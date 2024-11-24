import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit{
  isRecommendationsEmpty: boolean = false; // Default value is false (i.e., not empty)

  constructor(private userService: UserService) { }

  ngOnInit(): void {
    // Get user data from UserService
    const user = this.userService.getUser();

    // Check if user exists and recommendations list is available
    if (user && user.recommendations && user.recommendations.length > 0) {
      // If recommendations are not empty, set to false
      this.isRecommendationsEmpty = false;
    } else {
      // If recommendations are empty, set to true
      this.isRecommendationsEmpty = true;
    }
  }
}
