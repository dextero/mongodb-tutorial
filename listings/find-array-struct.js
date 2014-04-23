// przyklad: znajdz osoby, ktore maja dziecko o imieniu Jan oraz czarne zwierze
db.users.find({ dzieci: 'Jan',
                zwierzeta: {
                  $elemMatch: {
                    kolor: 'czarny'
                  }
                }
              })
