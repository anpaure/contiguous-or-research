# Ideal containment slots need at most `d+1` rows, and `d` rows miss only the triangular boundary

Date: 2026-08-01  
Status: unconditional all-`k` containment-matching theorem and exact Hall
deficiency bound.  It is an ideal owner-slot result, not a chain partition,
source chronology, or OR-word construction.

## 0. Statement

Put

\[
 r=\lceil k/2\rceil,\qquad W=\binom{k}{r},\qquad
 \Lambda=\sum_{s=1}^{r-1}\binom{k}{s},                 \tag{0.1}
\]

and

\[
 d=\min\left\{q:qW+\binom{q+1}{2}\ge\Lambda\right\},
 \qquad D=\left\lceil\frac{\Lambda}{W}\right\rceil. \tag{0.2}
\]

Let `L` be the nonempty strict lower ideal and make `q` labelled copies of
every rank-`r` set.  Join a lower target `S` to every copy of every `T`
containing `S`.

Then:

1. the `D`-copy graph has a matching saturating every lower target;
2. `d<=D<=d+1`;
3. the `d`-copy graph has matching deficiency at most

   \[
                  h=(\Lambda-dW)_+
                    \le\binom{d+1}{2};                \tag{0.3}
   \]

4. in particular, if `Lambda<=dW`, then already `D=d` and the `d`-copy
   graph saturates the complete lower ideal.

Thus no unbounded obstruction exists at the level of containment capacity
or ordinary Hall cuts.  The missing theorem is to chainize and serialize
these ideal assignments in one physical interval chronology.

## 1. Fractional containment matching

For a lower target `S` of rank `s`, and a rank-`r` superset `T`, assign

\[
 x_{S,(T,j)}=
 \frac{1}{D\binom{k-s}{r-s}}.                           \tag{1.1}
\]

There are `D binom(k-s,r-s)` neighbours, so the total flow out of `S` is
one.

At a fixed right vertex `(T,j)`, the incoming load is

\[
 \frac1D\sum_{s=1}^{r-1}
  \frac{\binom{r}{s}}{\binom{k-s}{r-s}}.               \tag{1.2}
\]

The elementary identity

\[
 \frac{\binom{r}{s}}{\binom{k-s}{r-s}}
  =\frac{\binom{k}{s}}{\binom{k}{r}}                  \tag{1.3}
\]

turns (1.2) into

\[
                         \frac{\Lambda}{DW}\le1.       \tag{1.4}
\]

Hence this is a fractional matching saturating the lower shore.  The
bipartite matching polytope is integral, proving item 1.

## 2. Relation between `D` and the deadline depth

Since `DW>=Lambda`, the integer `D` is admissible in (0.2), so `d<=D`.

For `k>=3`, `d<=r-1` and

\[
                         \binom{d+1}{2}\le W.           \tag{2.1}
\]

If `D>=d+2`, the ceiling definition gives

\[
 \Lambda>(D-1)W\ge(d+1)W
             \ge dW+\binom{d+1}{2},                   \tag{2.2}
\]

contradicting the definition of `d`.  The finitely small cases are direct.
Thus `D<=d+1`.

## 3. Exact deficiency with only `d` copies

There is a slightly stronger useful formulation.  Send unit flow from each
lower target `S` equally to its rank-`r` supersets, now without a copy
index:

\[
 y_{S,T}=\frac{1}{\binom{k-|S|}{r-|S|}}.               \tag{3.1}
\]

Every owner `T` receives the same load

\[
 \rho=\sum_{s=1}^{r-1}
  \frac{\binom{r}{s}}{\binom{k-s}{r-s}}
       =\frac{\Lambda}{W}.                             \tag{3.2}
\]

For any lower family `F`, all its flow enters the owner neighbourhood
`N(F)`.  Therefore

\[
                         |F|\le \rho |N(F)|.            \tag{3.3}
\]

In the graph with `d` copies per owner, Hall's deficiency is

\[
 \begin{aligned}
 \delta_d
 &=\max_F\bigl(|F|-d|N(F)|\bigr)_+\\
 &\le\max_F (\rho-d)|N(F)|\\
 &\le(\rho-d)_+W
   =(\Lambda-dW)_+=h.                                  \tag{3.4}
 \end{aligned}
\]

By the deficiency form of Hall, a matching misses at most `h` lower
targets.  The defining inequality for `d` gives (0.3).

## 4. Exact scope: slots are not chains

The theorem assigns each lower target to a distinct pair `(T,j)` with
`S subset T`.  It does **not** imply that the targets assigned to one owner
`T` are nested.  A physical word groups lower witnesses by endpoints, and
the ORs ending at one endpoint form one inclusion chain.  Therefore the
required strengthening is not another capacity matching but a chain-valued
matching:

* each rank-`r` owner receives at most about `d` lower targets;
* those targets must be nested;
* the owner chains must be serializable by one common move-to-front/source
  chronology; and
* the same chronology must retain the upper interval language and
  residence.

The previously proved deadline-depth lemma implies that in a word of length
`W+e`, every strict-lower witness may be chosen among intervals of length at
most `e`.  Grouping chosen witnesses by their right endpoint then partitions
the lower ideal into at most `W+e` chains of size at most `e`.  This is the
correct endpoint-chain consequence.  One should not replace that lemma by
the stronger unproved assertion that every interval of length `e+1`
contains a preselected middle witness.

## 5. Relation to the serial birail route

The ideal theorem removes scalar capacity and ordinary containment Hall as
possible sources of an unbounded additive gap.  It does not replace the
terminal physical compiler.  Two routes remain logically distinct:

1. **chainization:** round the ideal containment assignment into bounded
   nested endpoint chains and serialize them; or
2. **serial descent:** use physically closed birail comparators to move the
   terminal occurrence assignment into the antitone zero-/bounded-defect
   state of
   `MATH_THEOREM_ANTITONE_BIRAIL_HALL_OPTIMUM_AND_FOLDED_C8_COMPARATOR_GATE_20260801.md`.

The quotient-folded C8 carrier now supplies the correct local all-depth
comparator shape for route 2.  Owner-legal ray-host planting, cut repair,
matching closure, and comparator transport remain the exact physical gap.

