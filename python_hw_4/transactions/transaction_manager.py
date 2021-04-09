from functools import reduce
import pickle


class InvalidTransactionException(Exception):
    pass

class TransactionManager:
    @staticmethod
    def process_transaction():
        transactions = "\n".join(iter(input, "quit"))
        transaction_dict = {}
        for line in transactions.split('\n'):
            k, v = [word.strip() for word in line.rsplit(' ', 1)]
            if k in transaction_dict.keys():
                transaction_dict[k] = int(transaction_dict[k])+int(v)
            else:
                transaction_dict[k] = v
        list_of_all_transactions = [int(i) for i in transaction_dict.values()]
        summary = reduce(lambda x, y: x + y, list_of_all_transactions)
        with open('metadata.pkl', 'wb') as f:
            pickle.dump(transaction_dict, f)

        with open('metadata.pkl', 'rb') as f:
            loaded_info = pickle.load(f)
        print(loaded_info)
        print(f"потрачено всего: {summary} ")


