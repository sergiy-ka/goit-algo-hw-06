# Список укр.банків

def bank_names():
    bank_names = ['Ukrsib', 'Pumb', 'Raif', 'Kredo',
                  'OTP', 'Privat', 'Mono']
    return bank_names

# Офшорний банк


def offshore_bank():
    offshore_bank = 'Hermes'
    return offshore_bank

# Вартість транзакції між банками


def bank_trn_cost(bank1, bank2):
    bank_trn_cost = {
        'Ukrsib': {'Ukrsib': 0, 'Pumb': 1, 'Raif': 5, 'Kredo': 5, 'OTP': 4, 'Privat': 5, 'Mono': 10},
        'Pumb':   {'Ukrsib': 1, 'Pumb': 0, 'Raif': 0, 'Kredo': 5, 'OTP': 1, 'Privat': 4, 'Mono': 5},
        'Raif':   {'Ukrsib': 5, 'Pumb': 0, 'Raif': 0, 'Kredo': 4, 'OTP': 2, 'Privat': 4, 'Mono': 6},
        'Kredo':  {'Ukrsib': 5, 'Pumb': 5, 'Raif': 4, 'Kredo': 0, 'OTP': 7, 'Privat': 7, 'Mono': 1},
        'OTP':    {'Ukrsib': 4, 'Pumb': 1, 'Raif': 2, 'Kredo': 7, 'OTP': 0, 'Privat': 2, 'Mono': 3},
        'Privat': {'Ukrsib': 5, 'Pumb': 4, 'Raif': 4, 'Kredo': 7, 'OTP': 2, 'Privat': 0, 'Mono': 0},
        'Mono':   {'Ukrsib': 10, 'Pumb': 5, 'Raif': 6, 'Kredo': 1, 'OTP': 3, 'Privat': 0, 'Mono': 0, 'Hermes': 20},
        'Hermes': {'Hermes': 0, 'Mono': 20}
    }
    return bank_trn_cost[bank1][bank2]
