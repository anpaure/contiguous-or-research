# Independent audit: OFHT Ferrers top-rail Hall theorem

Date: 2026-08-01  
Audited file:
`MATH_THEOREM_R_OFHT_FERRERS_TOP_RAIL_STAR_HALL_AND_ANTI_NIBBLE_20260801.md`  
Verdict: **PASS after four scope corrections incorporated in the audited
file.**

## 1. Claims replayed

For `k in {2r-1,2r}` and
`L<=min(d,r-d-1)`, the exact top target rows give

\[
 |B_L|\ge W\left(1-\frac1r\sum_{j=1}^Lj^2\right).
\]

The two parity products are respectively

\[
 \prod_{i=0}^{j-1}\frac{r-i}{r+i+1},\qquad
 \prod_{i=0}^{j-2}\frac{r-1-i}{r+1+i},
\]

and the stated `j^2/r` loss bounds follow termwise.  On strict positive-age
states, consecutive marks at ranks `r-L,...,r-1` force the final `L` age
cells to be singletons.

The literal recurrence then forces an ordered `(L-1)`-cell suffix in every
positive successor, and terminal-star geometry leaves exactly `k-r`
external owner fibres.  The exact uniform slice of any compatible fixed
type fibre is

\[
                         1/(r)_{L-1}.
\]

Therefore conditional `K`-spread gives

\[
                         \mu_L=K(k-r)/(r)_{L-1},
\]

and Markov's inequality gives the theorem's Hall-deficiency bound.  No
independence between different external owner fibres is used.

The two-bank criterion

\[
                         r_{M_B}(S)+r_{M_C}(S)\ge |S|
\]

is valid for the declared partition of the tail bank.  It is matroid union,
equivalently common-base intersection of `M_C` with `M_B^*`; it is not a
generic common-base assertion for `M_B` and `M_C` themselves.

## 2. Corrections incorporated

1. A formal aggregate `e_0` role is not automatically a full-source state.
   The original construction can realize it by the strict positive state
   `(r-d,1,...,1)` marked nowhere.  The theorem now states the exact
   strict-or-full-source template hypothesis.
2. A full-source loop is forced only when the declared role relation admits
   its self-edge; otherwise it is itself a singleton obstruction.  The
   original Hall cut corresponding to a contracted cut `A` is
   `A union Z`.
3. The owner-plus-suffix rail graph is only a necessary supergraph.  The
   exact rail transversal matroid uses the full literal recurrence.  The
   audited file now includes a four-coordinate counterexample to replacing
   it by the supergraph.
4. The successor-fibre amplification statement now uses weighted averaging
   over external owner/type probabilities rather than an unweighted
   pigeonhole.

## 3. Scope

The theorem rigorously rules out product and bounded-conditional-bias
ownerwise nibbles, even though the Ferrers role banks are exponential.  It
does not rule out OFHT: exact nested-target conditioning can create the
superpolynomial chronology correlation which the theorem proves necessary.
