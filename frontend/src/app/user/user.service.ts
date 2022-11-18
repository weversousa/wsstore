import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable } from 'rxjs';
import { User } from './user.model';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  URL: string = 'http://localhost:5000/api/users';

  constructor(private http: HttpClient) { }

  createUser(user: User) {
    return this.http.post(this.URL, user);
  }

  updateUser(user: User) {
    return this.http.put('http://localhost:5000/api/users?id=6', user);
  }

  updateUserPassword(password: string) {
    return this.http.put('http://localhost:5000/api/users?id=6', password);
  }

  readUser(): Observable<User[]> {
    return this.http.get<User[]>(this.URL);
  }

  // getUsers(user: User) {
  //   return this.http.get(this.URL);
  // }
}
