//
//  Helper.swift
//  meal-tracker-ios
//
//  Created by Spencer Merryman on 9/26/18.
//  Copyright © 2018 Spencer Merryman. All rights reserved.
//

import Foundation
import UIKit

class Helper {
    static func showAlert(viewController:UIViewController,title:String?,message:String?) {
        let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
        let dismiss = UIAlertAction(title: "Dismiss", style: .default, handler: nil)
        alert.addAction(dismiss)
        viewController.present(alert, animated: true, completion: nil)
    }
}
