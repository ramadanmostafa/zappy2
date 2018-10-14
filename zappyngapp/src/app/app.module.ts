import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { TweetsListComponent } from './tweets-list/tweets-list.component';
import { TweetService } from './tweet.service'

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent,
    TweetsListComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [TweetService],
  bootstrap: [AppComponent]
})
export class AppModule { }
