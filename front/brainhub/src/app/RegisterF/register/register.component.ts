import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';
import { UserService } from '../../services/user.service';
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})
export class RegisterComponent {
  username: string = '';
  email: string = '';
  password: string = '';
  
  constructor(private authService: AuthService,private router: Router ,private userService: UserService) {}

  onSubmit() {
    this.authService.register(this.username, this.email, this.password).subscribe(
      
      (response) => {
        console.log('Registration successful:', response);
        alert(response.message);
        this.router.navigate(['/login']);
      },
      (error) => {
        console.error('Registration failed:', error);
        alert(error.error);
      }
    );
  }
}
