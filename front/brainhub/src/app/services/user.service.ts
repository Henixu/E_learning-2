import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor() { }

  // Set user data in localStorage
  setUser(userData: any) {
    if (typeof window !== 'undefined' && window.localStorage) {
      localStorage.setItem('learner', JSON.stringify(userData)); // Store as string
    }
  }

  getUser() {
    if (typeof window !== 'undefined' && window.localStorage) {
      // Use localStorage only if available
      const user = localStorage.getItem('learner');
      return user ? JSON.parse(user) : null;
    }
    return null;  // Return null or appropriate fallback if not in a browser environment
  }

  // Remove user data from localStorage (e.g., on logout)
  removeUser() {
    if (typeof window !== 'undefined' && window.localStorage) {
      localStorage.removeItem('learner');
    }
  }
}
