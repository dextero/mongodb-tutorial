db.users.find({ dzieci: 'Jan',
                zwierzeta: {
                  $elemMatch: {
                    kolor: 'czarny'
                  }
                }
              })
