
(require '[clojure.set :as set])

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

(def visited1 (loop [i 0  loc [0 0] locs (set [[0, 0]])]
                   (if (>= i steps) locs
                   (recur (+ i 2) (addLoc loc (moves i)) (conj locs (addLoc loc (get moves i)))))))
                   
(def visited2 (loop [i 1  loc [0 0] locs (set [[0, 0]])]
                   (if (>= i steps) locs
                   (recur (+ i 2) (addLoc loc (moves i)) (conj locs (addLoc loc (get moves i)))))))
    
(def totalVisited (set/union visited1 visited2))
    
(def result (count totalVisited))
(println result)