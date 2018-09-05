//
//  User.swift
//  meal-tracker-ios
//
//  Created by Spencer Merryman on 9/5/18.
//  Copyright © 2018 Spencer Merryman. All rights reserved.
//

import Foundation

struct User:Codable {
    static var current:User!
    var id:String
    var username:String
}
