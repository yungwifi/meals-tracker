//
//  HomePageViewController.swift
//  meal-tracker-ios
//
//  Created by Spencer Merryman on 9/5/18.
//  Copyright © 2018 Spencer Merryman. All rights reserved.
//

import Foundation
import UIKit
import Alamofire

class HomePageViewController:UITableViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    func getMeals(){
        Alamofire.request(API_HOST+"/meals", method:.get, parameters:nil).responseData {
            response in
            switch response.result{
            case .success(let data):
                do {
                    self.mealData = try JSONDecoder().decode(mealData.self, from: data)
                    self.tableView.reloadData()
                } catch {
                    Helper.showAlert(viewController: self, title: "Oops!", message: error.localizedDescription)
                }
            case .failure(let error):
                Helper.showAlert(viewController: self, title: "Oops!", message: error.localizedDescription)
            }
        }
    }
    
}
