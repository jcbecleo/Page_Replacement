class LFUPageReplacement:
    def __init__(self, capacity):
        self.capacity = capacity
        self.frames = []
        self.page_hits = 0
        self.page_faults = 0
        self.memory_states = []
        self.hit_fault = []
        self.page_frequencies = {}

    def access_page(self, reference_string):
        for page in reference_string:
            if page not in self.frames:
                if len(self.frames) < self.capacity:
                    self.frames.append(page)
                    self.page_frequencies[page] = 1
                else:
                    # Find the page with the minimum frequency
                    min_page = min(self.page_frequencies, key=self.page_frequencies.get)
                    self.frames[self.frames.index(min_page)] = page
                    self.page_frequencies.pop(min_page)
                    self.page_frequencies[page] = 1

                self.page_faults += 1
                self.hit_fault.append('F')
            else:
                self.page_frequencies[page] += 1
                self.page_hits += 1
                self.hit_fault.append('H')

            self.memory_states.append(list(self.frames))

    def display_memory_state(self, page_len):
        prefix = "|"
        prefix1 = "---+"

        print("+----------+" + prefix1 * page_len)
        for i in range(self.capacity):
            print(prefix, f"Frame {i + 1}:", end=" | ")
            print(" | ".join(str(state[i]) if i < len(state) else " " for state in self.memory_states), end=" | ")
            print()
            print("+----------+" + prefix1 * page_len)

        prefix2 = "\t"
        print(prefix2, end="     ")
        for hit_fault in self.hit_fault:
            print(hit_fault, end="   ")

        print()
        print(f"\nPage Hits: {self.page_hits}\nPage Faults: {self.page_faults}")
        print(f"\nPage Hit Ratio: {(self.page_hits / page_len) * 100}%\nPage Fault Ratio: {(self.page_faults / page_len)* 100}%")

if __name__ == "__main__":
    print("+------------------------------------------------+")
    print("|   Least Frequently Used (LFU) Page Replacement |")
    print("+------------------------------------------------+")
    lfu = LFUPageReplacement(3)

    reference_string = [7, 0, 1, 2, 0, 3, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7]

    print("Reference String: ", end="")
    for p in reference_string:
        print(f"{p}  ", end="")
    print("\n")

    page_len = len(reference_string)

    lfu.access_page(reference_string)

    lfu.display_memory_state(page_len)