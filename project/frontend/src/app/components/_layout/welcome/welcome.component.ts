import { Component, OnInit } from '@angular/core';
import { DotLottie } from '@lottiefiles/dotlottie-web';


@Component({
  selector: 'app-welcome',
  imports: [],
  templateUrl: './welcome.component.html',
  styleUrl: './welcome.component.scss'
})
export class WelcomeComponent implements OnInit {

  ngOnInit(): void {
    console.log('app connect')
    const canvas = document.querySelector('#dotlottie-canvas') as HTMLCanvasElement;

    if (canvas) {
      const dotLottie = new DotLottie({
        autoplay: true,
        loop: true,
        canvas,
        src: '../assets/animation.lottie', // use actual URL
      });
    } else {
      console.error('Canvas element not found');
    }
  }

}
