import { Component, OnInit, inject, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ButtonModule } from 'primeng/button';
import { HeaderComponent } from './components/_layout/header/header.component';
import { WelcomeComponent } from './components/_layout/welcome/welcome.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, ButtonModule, HeaderComponent, WelcomeComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent implements OnInit {
  loading = signal<boolean>(true)

  ngOnInit(): void {
    setTimeout(() => {
      this.loading.set(false);
    }, 2000);
  }
}
