import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './LoginF/login/login.component';
import { FormsModule } from '@angular/forms';
import { RegisterComponent } from './RegisterF/register/register.component';
import { HomeComponent } from './HomeF/home/home.component';
import { NavbarComponent } from './NavbarF/navbar/navbar.component';
import { FooterComponent } from './FooterF/footer/footer.component';
import { ProfileComponent } from './ProfileF/profile/profile.component';
import { PopupComponent } from './popup/popup.component';
@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    HomeComponent,
    NavbarComponent,
    FooterComponent,
    ProfileComponent,
    PopupComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    
  ],
  providers: [
    provideClientHydration()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
