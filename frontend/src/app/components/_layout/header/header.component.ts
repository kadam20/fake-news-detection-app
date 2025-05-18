import { Component, OnInit, inject, signal } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { LayoutService } from '../../../services/layout.service';
import { LocalstorageService } from '../../../services/localstorage.service';
import { Router } from '@angular/router';
import { RouteEnums } from '../../../enums/route.enum';

@Component({
  selector: 'app-header',
  imports: [ButtonModule],
  standalone: true,
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss',
})
export class HeaderComponent implements OnInit {
  layoutService = inject(LayoutService);
  localStorageService = inject(LocalstorageService);
  routeEnums = RouteEnums;
  isDarkMode = this.layoutService.isDarkMode;
  currentTab = signal<string>(this.routeEnums.DIRECT_TEXT);
  loading = signal<boolean>(true);

  constructor(private router: Router) {}

  ngOnInit(): void {
    setTimeout(() => {
      this.loading.set(false);
    }, 2000);
    // Get the current tab from local storage and set it to the current tab.
    const currentTab = this.localStorageService.getItem('currentTab');
    if (currentTab) {
      this.currentTab.set(currentTab);
      this.router.navigate([`/${currentTab}`])
    }
  }

  /**
   * Toggles the dark mode of the header component.
   */
  toggleDarkMode() {
    this.layoutService.toggleDarkMode();
  }

  /**
   * Navigates to the specified tab.
   * @param {string} tabName - The name of the tab to navigate to.
   */
  navigateTab(tabName: string) {
    this.currentTab.set(tabName);
    this.router.navigate([`/${tabName}`])
    this.localStorageService.setItem('currentTab', tabName);
  }
}
