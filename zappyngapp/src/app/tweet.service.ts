
import {throwError as observableThrowError,  Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { ITweet } from './tweet';
import { tap, catchError } from 'rxjs/operators';



@Injectable()
export class TweetService {

  private _url: string = "http://127.0.0.1:8000/api/tweets/v1/list/";

  constructor(private http:HttpClient) { }

  getTweets(): Observable<ITweet[]>{
    return this.http.get<ITweet[]>(this._url)
                    .pipe(tap(data => data) , catchError(this.errorHandler))
  }
  errorHandler(error: HttpErrorResponse){
    return observableThrowError(error.message || "Server Error");
  }

}
