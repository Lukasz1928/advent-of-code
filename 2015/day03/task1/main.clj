
(def readInput (fn [] (slurp "input")))

(def char2dir (fn [c] (case c
                       \^ [0 1]
                       \v [0 -1]
                       \< [-1 0]
                       \> [1 0]
                       [0 0]
)))

(def data (readInput))

(def moves (vec (map char2dir data)))

(def steps (count moves))

(def addLoc (fn [loc d] [(+ (get loc 0) (get d 0)) (+ (get loc 1) (get d 1))]))

(def visited (loop [i 0  loc [0 0] locs (set [[0, 0]])]
                   (if (= i steps) locs
                   (recur (inc i) (addLoc loc (moves i)) (conj locs (addLoc loc (get moves i)))))))
    

(def result (count visited))
(println result)