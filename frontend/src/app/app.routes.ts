import { Routes } from '@angular/router';
import { RouteEnums } from './enums/route.enum';
import { DirectComponent } from './components/direct/direct.component';
import { ArticleComponent } from './components/article/article.component';
import { AboutComponent } from './components/about/about.component';

export const routes: Routes = [
    { path: RouteEnums.DIRECT_TEXT, component: DirectComponent },
    { path: RouteEnums.ARTICLE_TEXT, component: ArticleComponent },
    { path: RouteEnums.ABOUT, component: AboutComponent },
    { path: '**', redirectTo: RouteEnums.DIRECT_TEXT },
];
