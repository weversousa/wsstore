import { Component, OnInit } from '@angular/core';
import { User } from './user.model';
import { UserService } from './user.service';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {

  constructor(private userService: UserService) { }

  ngOnInit(): void {
    // this.createUser();
    // this.readUser();
    this.updateUser();
  }

  createUser(): void {
    this.userService
      .createUser({email: 'jaqueline@gmail.com', password: '1234'})
      .subscribe((res) => console.log(res));
  }

  updateUser(): void {
    this.userService
      .updateUser({email: 'jaques@gmail.com', password: '5678'})
      .subscribe((res) => console.log(res));
  }

  updateUserPassword(): void {
    this.userService
      .updateUserPassword('0000')
      .subscribe((res) => console.log(res));
  }

  readUser(): void {
    this.userService
      .readUser()
      .subscribe(res => console.log(res));
  }
}
