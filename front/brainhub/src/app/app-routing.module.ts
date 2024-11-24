import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './LoginF/login/login.component';
import { RegisterComponent } from './RegisterF/register/register.component';
import { ProfileComponent } from './ProfileF/profile/profile.component';
import { HomeComponent } from './HomeF/home/home.component';

const routes: Routes = [{ path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'profile', component: ProfileComponent },
  { path: 'home', component: HomeComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' }, 
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
