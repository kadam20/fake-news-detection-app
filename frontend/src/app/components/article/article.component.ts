import { Component, NgZone, signal } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { FormsModule } from '@angular/forms';
import { InputTextModule } from 'primeng/inputtext';
import { ProgressBar } from 'primeng/progressbar';


@Component({
  selector: 'app-article',
  imports: [ButtonModule, FormsModule, InputTextModule, ProgressBar],
  templateUrl: './article.component.html',
  styleUrl: './article.component.scss'
})
export class ArticleComponent {
  pageState = signal<string>('normal');
  value = signal<number>(0);
  textValue = signal<string>('');
  result = signal<any>(null);
  interval: any;
  isValid = signal<boolean>(false);
  precision = signal<number>(0);

  constructor(private ngZone: NgZone) {}

  removeText() {
    this.textValue.set('');
  }

  analyzeText() {
    this.pageState.set('loading');
    this.value.set(0);
    this.result.set(null);
    this.textValue.set('');
    this.isValid.set(false);
    this.precision.set(0);
    const preci = this.value() + Math.floor(Math.random() * 100) + 1;
    this.precision.set(preci);
    if(preci > 50) {
      this.isValid.set(true);
    } 
    this.ngZone.runOutsideAngular(() => {
      this.interval = setInterval(() => {
        this.ngZone.run(() => {
          const newValue = this.value() + Math.floor(Math.random() * 20) + 1;
          this.value.set(newValue);
          console.log('New value:', newValue);
          if (this.value() >= 100) {
            this.value.set(100);
            clearInterval(this.interval);
            this.pageState.set('result');
          }
        });
      }, 1000);
    });
  }

  refresh() {
    this.pageState.set('normal');
    this.value.set(0);
    this.result.set(null);
    this.textValue.set('');
    this.isValid.set(false);
    this.precision.set(0);
  }

  ngOnDestroy() {
    if (this.interval) {
      clearInterval(this.interval);
    }
  }

}
