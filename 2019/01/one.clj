;; calculates fuel for a mass
(defn fuel-counter [mass] (int (- (Math/floor (/ mass 3)) 2)))


;; total fuel calc
;; https://gitlab.com/imhoffman/fa19b4-mat3006/raw/master/code/day17/2019_01_one.clj
(defn total-fuel [list-of-masses accum]
  (if (empty? list-of-masses)
    accum
    (recur (rest list-of-masses) (+ accum (fuel-counter (first (int list-of-masses)))))))


;; main program

;; input is the contents of input.txt
(def input
  (with-open [f (clojure.java.io/reader "input.txt")]
    (reduce conj () (line-seq f))))      

;; answer
;; https://gitlab.com/imhoffman/fa19b4-mat3006/raw/master/code/day17/2019_01_one.clj
(println
  " part one: the fuel needed for the module masses is"
  (total-fuel input 0))


