import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css'
})
export class ProfileComponent implements OnInit {
  
  cours = [
    { date: '21 Jun, 2021', title: 'Marketing', description: 'Every Marketing Plan Needs', status: 'Pending' },
    { date: '13 Aug, 2021', title: 'Website Design', description: 'Creating the design and layout of a website.', status: 'Completed' },
    { date: '08 Sep, 2021', title: 'UI / UX Design', description: 'Plan and conduct user research and analysis.', status: 'In Progress' },
    { date: '10 Oct, 2021', title: 'Graphic Design', description: 'Creating graphics for various marketing campaigns.', status: 'Pending' },
];

skills = ['HTML', 'CSS', 'JavaScript', 'Machine Learning', 'AI'];
constructor(private userService: UserService) {}
  user: any;
  ngOnInit() {
    // Fetch user data from localStorage or UserService
    this.user = this.userService.getUser();
    //affichier user
    console.log(this.user?.learner?.username, 'user object alex');
  }

}
