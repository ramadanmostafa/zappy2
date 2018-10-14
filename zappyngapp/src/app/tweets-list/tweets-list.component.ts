import { Component, OnInit } from '@angular/core';
import { TweetService } from '../tweet.service';
import './tweets-list.component.css'

@Component({
  selector: 'list-tweets',
  template: `
    <h2>Tweets List</h2>
    <h3>{{errorMsg}}</h3>
    <table style="width:100%">
      <tr>
        <th>Tweet ID</th>
        <th>Username</th>
        <th>Language</th>
        <th>Date Created</th>
        <th>Text</th>
        <th>Is retweeted?</th>
        <th>Retweets Count</th>
      </tr>
      <tr *ngFor="let tweet of tweets">
        <td>{{ tweet.tweet_id }}</td>
        <td>{{ tweet.user_name }}</td>
        <td>{{ tweet.lang }}</td>
        <td>{{ tweet.created_at }}</td>
        <td>{{ tweet.text }}</td>
        <td>{{ tweet.retweeted }}</td>
        <td>{{ tweet.retweet_count }}</td>
      </tr>
    </table>
  `,
  styles: []
})
export class TweetsListComponent implements OnInit {

  public tweets = [];
  public errorMsg;
  constructor(private _tweetService: TweetService) { }

  ngOnInit() {
    this._tweetService.getTweets()
      .subscribe(data => this.tweets = data,
                error => this.errorMsg = error);
  }



}
