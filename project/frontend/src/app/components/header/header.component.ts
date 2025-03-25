import { Component, OnInit, inject, signal } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { LayoutService } from '../../services/layout.service';
import { LocalstorageService } from '../../services/localstorage.service';
import { Router } from '@angular/router';

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

  isDarkMode = this.layoutService.isDarkMode;

  constructor(private router: Router) {}

  ngOnInit(): void {}

  /**
   * Toggles the dark mode of the header component.
   */
  toggleDarkMode() {
    this.layoutService.toggleDarkMode();
  }
}
