import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { UserService } from '../../services/user.service';
import { Router } from '@angular/router';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'] // Ensure this is plural
})
export class LoginComponent {
  email: string = '';
  password: string = '';
  isLoading: boolean = false; // Add this line
  errorMessage: string = ''; // Optional: Add this line to handle error messages

  constructor(private authService: AuthService,private router: Router ,private userService: UserService) {}

  // Call login method on form submission
  onSubmit() {
    this.isLoading = true;
    this.authService.login(this.email, this.password).subscribe(
      (response) => {
        this.isLoading = false;
        console.log('Login successful:', response);
        // Save user details and other data in a service or local storage
        this.userService.setUser(response); 
        console.log(this.userService.getUser());
        this.router.navigate(['/home']);
      },
      (error) => {
        this.isLoading = false;
        this.errorMessage = 'Invalid email or password.';
        alert('Invalid email or password.');
      }
    );
  }
}
