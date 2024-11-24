import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://localhost:8000/login'; // Replace with your Django API URL
  private registerUrl = 'http://localhost:8000/register'; // Replace with your Django API URL
  constructor(private http: HttpClient) {}

  
  login(email: string, password: string): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = { email, password };  // Ensure 'email' is used here

    // Sending POST request to Django backend
    return this.http.post(this.apiUrl, body, { headers });
}

register(username: string, email: string, password: string): Observable<any> {
  const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
  const body = { username, email, password };
  return this.http.post(this.registerUrl, body, { headers });
}
}
