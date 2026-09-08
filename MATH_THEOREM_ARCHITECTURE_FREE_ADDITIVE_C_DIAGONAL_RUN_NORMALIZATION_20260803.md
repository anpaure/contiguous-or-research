# Architecture-free additive-C diagonal rows and the global density barrier

**Date:** 2026-08-03  
**Status:** unconditional for every universal nonzero OR word of length
`W+d(k)+C`; no carrier, Johnson, flat-row, or cyclic hypothesis is used.
The conclusion is a qualitative `Omega_C(rW)` occurrence-density theorem,
not the sharp resident-carrier constant and not a construction theorem.

## 0. Outcome

Put

\[
 r=\left\lceil{k\over2}\right\rceil,
 \qquad W={k\choose r},
 \qquad
 \Lambda=\sum_{s=1}^{r-1}{k\choose s},
 \qquad
 M=\sum_{s=1}^{r-1}s{k\choose s},
\]

and let `d=d(k)` be least with

\[
 dW+{d+1\choose2}\ge\Lambda.
\]

Fix `C>=0`, put `e=d+C`, and let

\[
 A=(A_1,\ldots,A_{W+e})
\tag{0.1}
\]

be an arbitrary universal word whose letters are nonempty subsets of
`[k]`.  Define its literal coordinate-occurrence mass by

\[
 P(A)=\sum_{i=1}^{W+e}|A_i|.
\tag{0.2}
\]

Then, for every fixed `C`, there are constants `c_C>0` and `k_C` such
that

\[
 \boxed{P(A)\ge c_C rW\qquad(k\ge k_C).}
\tag{0.3}
\]

Thus the positive linear-density conclusion previously known for a fixed
resident carrier is in fact architecture-free.  In particular, no
`B(k)+C` word can be supported by a fixed number of sparse residue rails
whose total occurrence mass is `O_C(rW/d)`.

The normalization behind (0.3) is also explicit.

* The `W` middle targets admit ordered first-witness intervals which split
  into at most `2e+1` diagonal blocks.  On each block there is a literal
  fixed-depth row
  \[
       T_j=A_j\cup\cdots\cup A_{j+h}
       \in{[k]\choose r}.
  \]
* Trimming at most `h` owners from the right of every block makes the
  source spans of the blocks disjoint.  The total number of discarded
  lower cells is `O(e^3)`, hence polynomial in `k`.
* After additionally discarding the blocks of depth below `e/2`, the
  retained rows contain
  \[
       W-O_C(W/e)
  \]
  distinct middle owners and their proper-prefix cells represent every
  strict-lower target except `O_C(W)` of them.
* These retained rows have only `O_C(W)` positive coordinate runs in
  total, hence only `O_C(1)` coordinate births per owner transition on
  average.  Their literal occurrence markers nevertheless have total mass
  `Omega_C(rW)`.

There is also a macroscopic normal form.  For every fixed `eta>0`, after
deleting at most `eta W+o(W)` selected owners, the remaining selected
intervals form

\[
 O_C(1/\eta)
\]

diagonal fixed-depth rows, each of depth at least
`e-O_C(1/eta)`.  This is the strongest bounded-piece extraction forced by
the endpoint ledger alone.  It does **not** force Johnson adjacency or
`W+O_C(1)` runs.

## 1. Ordered first witnesses

Choose one witnessing interval for each rank-`r` target.  If its start is
`a`, replace its right endpoint by the least `b` for which
`A_a union ... union A_b` has rank `r`.  The value does not change: this
least prefix is contained in the old rank-`r` value and has the same rank,
so the two sets are equal.  In particular, its `b-a` proper prefixes are
exactly the strict-lower cells in column `a`.

Write the resulting intervals, ordered by their starts, as

\[
 I_t=[a_t,b_t],\qquad T_t=\bigcup_{i=a_t}^{b_t}A_i,
 \qquad 1\le t\le W.
\tag{1.1}
\]

### Lemma 1.1 (strict endpoint order)

Both endpoint sequences are strictly increasing:

\[
 a_1<\cdots<a_W,
 \qquad b_1<\cdots<b_W.
\tag{1.2}
\]

Moreover, putting `L=W+e`,

\[
 t\le a_t,b_t\le t+e.
\tag{1.3}
\]

#### Proof

Two intervals with the same start are nested and therefore cannot have
different equal-rank union values.  If two intervals with increasing
starts had nonincreasing ends, they would again be nested.  This proves
(1.2).  Every strictly increasing `W`-tuple in `[L]` has its `t`-th term
between `t` and `L-W+t=t+e`, proving (1.3).  `square`

Put

\[
 x_t=a_t-t,
 \qquad y_t=b_t-t,
 \qquad z_t=e-y_t,
 \qquad h_t=b_t-a_t=e-x_t-z_t.
\tag{1.4}
\]

Then `x_t,y_t` are nondecreasing, `z_t` is nonincreasing, and all three
displayed displacement variables lie in `[0,e]`.

### Lemma 1.2 (exact displacement budget)

Let

\[
 \epsilon_k={dW-\Lambda\over W}.
\tag{1.5}
\]

Then

\[
 \boxed{
 \sum_{t=1}^W(x_t+z_t)
 \le (C+\epsilon_k)W+e^2.}
\tag{1.6}
\]

In particular, for fixed `C`, the right side is `O_C(W)`.

#### Proof

There are exactly `e` unselected start columns.  By the monotone-deadline
depth cap, every column contains at most `e` strict-lower cells.  Hence at
most `e^2` strict-lower targets can have all their witnesses in unselected
columns.

At selected column `a_t`, the proper prefixes of `I_t` give exactly `h_t`
strict-lower cells.  Therefore

\[
 \sum_t h_t\ge\Lambda-e^2.
\tag{1.7}
\]

Now use `h_t=e-x_t-z_t` and `eW-\Lambda=(C+\epsilon_k)W`.
If `d=0`, then `epsilon_k=0`.  If `d>=1`, minimality of `d` gives the
exact inequality

\[
 (d-1)W+{d\choose2}<\Lambda,
 \qquad\text{hence}\qquad
 \epsilon_k<1-{1\over W}{d\choose2}<1.
\]

Thus, for fixed `C`, the right side of (1.6) is `O_C(W)`.  `square`

### Corollary 1.3 (macroscopic bounded-piece extraction)

For every `K>=0`, deleting at most

\[
 {2((C+\epsilon_k)W+e^2)\over K+1}
\tag{1.8}
\]

selected owners leaves one interval of indices on which

\[
 x_t\le K,qquad z_t\le K.
\tag{1.9}
\]

That interval splits into at most `2K+1` diagonal blocks, and every block
has depth at least `e-2K`.

#### Proof

The set where `z_t>K` is a prefix and the set where `x_t>K` is a suffix.
Markov's inequality and (1.6) give (1.8).  On what remains, each of the
two integer monotone sequences can jump at most `K` times.  Between their
jumps both endpoints advance by one, and `h_t=e-x_t-z_t` is constant.
`square`

Taking `K=O_C(1/eta)` proves the macroscopic statement in Section 0.

## 2. Exact diagonal decomposition and disjoint source cores

Split `[W]` at every `t` for which either

\[
 a_{t+1}>a_t+1
 \quad\hbox{or}\quad
 b_{t+1}>b_t+1.
\tag{2.1}
\]

### Lemma 2.1 (few literal rows)

There are at most `2e+1` resulting blocks.  On a block of length `m` there
is a constant `h` such that, after translating indices,

\[
 T_j=A_j\cup A_{j+1}\cup\cdots\cup A_{j+h},
 \qquad 1\le j\le m,
\tag{2.2}
\]

and the `T_j` are distinct rank-`r` sets.

#### Proof

The total excess in the start gaps is at most

\[
 a_W-a_1-(W-1)\le e,
\]

and the same holds for the end gaps.  Thus (2.1) creates at most `2e`
cuts.  Between cuts both endpoints advance by one, proving (2.2).  The
labels are the selected distinct middle targets.  `square`

For a block of depth `h`, retain only its first `(m-h)_+` owners.  The
source span needed by those retained owners ends at the final **start** of
the original block.  Since the start intervals of successive blocks are
disjoint and ordered, these trimmed source spans are pairwise disjoint.

The trimming deletes at most `h^2` proper-prefix cells from one block.
Consequently, over all blocks it deletes at most

\[
 D_0:=e^2+(2e+1)e^2=O(e^3)
\tag{2.3}
\]

target cells, including the `e^2` unselected-column allowance.

Let the trimmed blocks have lengths `n_b` and depths `h_b`, and put

\[
 N=\sum_b n_b,
 \qquad Q=\sum_bh_bn_b.
\tag{2.4}
\]

Then

\[
 N=W-O(e^2),
 \qquad Q\ge\Lambda-D_0,
\tag{2.5}
\]

and hence

\[
 \boxed{
 \sum_b(e-h_b)n_b=eN-Q
 \le(C+\epsilon_k)W+D_0.}
\tag{2.6}
\]

Call a trimmed block **deep** when `h_b>=e/2`.  Equations (2.5)--(2.6)
give

\[
 N_{\rm shallow}=O_C(W/e),
 \qquad Q_{\rm shallow}=O_C(W).
\tag{2.7}
\]

Therefore the proper-prefix cells in the deep blocks represent all but

\[
 \delta_C=O_C(W)
\tag{2.8}
\]

strict-lower targets.  If `H` denotes their total rank mass, then

\[
 \boxed{H\ge M-(r-1)\delta_C.}
\tag{2.9}

The estimates absorb the polynomial `D_0`, because `W` is exponential in
`k`.

## 3. A finite-row gap lemma

The following is the only local input needed below.

### Lemma 3.1 (clipped resident run)

Fix `h>=1`.  Let a source segment have length `n+h`, and put

\[
 T_j=\bigcup_{i=j}^{j+h}A_i,qquad1\le j\le n.
\tag{3.1}
\]

For one coordinate, decompose its positive trace in `T` into runs.

1. Every run not meeting an end of `[n]` has length at least `h+1`.
2. For every run of length `L>=h+1`, after adding at most two virtual
   endpoint markers when the run meets a boundary, its retained source
   markers have successive gaps `g<=h+1`, with
   \[
       \sum g=L-h-1.
   \tag{3.2}
   \]
3. Across the `h` proper-prefix rows, that run contributes at most
   \[
       h\left(L-{h+1\over2}\right)
       -\sum_g{g\choose2}+2h^2
   \tag{3.3}
   \]
   coordinate--cell incidences.  The `2h^2` term is needed only for a
   boundary run.
4. Runs of length below `h+1` meet a boundary.  Their total contribution
   is at most `h(h+1)` each.

#### Proof

For an internal run `[s,t]`, absence at `s-1` and presence at `s` force a
source occurrence at `s+h`; presence at `t` and absence at `t+1` force
one at `t`.  Positivity between them is exactly the assertion that
successive marker gaps are at most `h+1`.  This proves (1)--(2) internally.

For a boundary run of length at least `h+1`, adjoin the missing canonical
marker at `s+h` when `s=1`, or at `t` when `t=n` (both when the run meets
both boundaries).  Retain the actual markers between these canonical
endpoints.  Positivity of the owner trace implies that successive retained
or virtual markers are at distance at most `h+1`.  Actual markers discarded
to the left of `s+h` can affect only the first `h` source-window starts in
each prefix row, and those discarded to the right of `t` can affect only
the last `h`; their total contribution is therefore at most `2h^2`.

For the retained markers, a `q`-cell sees a marker in the usual union of
start intervals `[z-q+1,z]`.  Between markers at distance `g`, exactly
`(g-q)_+` starts are missed.  Summing over `q=1,...,h` gives

\[
 h\left(L-{h+1\over2}\right)-\sum_g{g\choose2},
\]

which proves (3).  Finally a short run can occur only at a boundary by
(1), and a `q`-prefix containing the coordinate is also a positive owner
position, so its contribution is at most `hL<h(h+1)`.  `square`

## 4. Architecture-free run and birth bounds

Apply Lemma 3.1 to every coordinate in every deep trimmed block.  Let

* `R` be the number of long positive coordinate runs;
* `L_+` be their total owner length;
* `J=sum_g binom(g,2)` over all augmented marker gaps;
* `G` be the number of those gaps;
* `S=sum_g g`.

There are at most two boundary runs per coordinate per block.  Since the
number of blocks is at most `2e+1`, every error caused by short or clipped
runs is

\[
 O(ke^3)=o(W).
\tag{4.1}
\]

The deep blocks contain `W-O_C(W/e)` owners, each of rank `r`.  Hence

\[
 L_+=rW-O_C(eW),
\tag{4.2}
\]

where `r/e=Theta(e)` was used.

Dropping `J` from (3.3), using `h_b>=e/2`, and summing gives

\[
 H\le erW-{e^2\over8}R+O(ke^3).
\tag{4.3}

On the other hand, (2.9) holds.  The standard central-binomial first
moment estimate gives

\[
 r\Lambda-M=O(kW).
\tag{4.4}

For completeness, (4.4) follows from Cauchy--Schwarz applied to
`Bin(k,1/2)` and the Wallis estimate `2^k=O(sqrt(k)W)`.  Also

\[
 eW-\Lambda=(C+\epsilon_k)W=O_C(W).
\tag{4.5}

Therefore

\[
 erW-M=O_C(kW).
\tag{4.6}

Equations (2.9), (4.3), and (4.6) prove

\[
 \boxed{R=O_C(W).}
\tag{4.7}

Adding the `O(ke)` boundary runs does not change this estimate.  Since a
transition between two distinct rank-`r` owners creates at least one new
positive coordinate run, (4.7) also proves an `O_C(1)` average birth
multiplicity on the retained rows.

This is the strongest run-count conclusion forced here.  It is an
`O_C(W)` bound, not `W+O_C(1)` and not Johnson adjacency.

## 5. Architecture-free occurrence density

For every augmented long run, (3.2) gives

\[
 S=L_+-\sum_{\rho=1}^{R}(h_\rho+1).
\tag{5.1}

By (4.2), (4.7), and `h_rho<=e`,

\[
 \boxed{S=rW-O_C(eW)=(1-o(1))rW.}
\tag{5.2}

Keeping the convex loss in Lemma 3.1 instead gives

\[
 J\le erW-H+O(ke^3)=O_C(kW).
\tag{5.3}

Convexity over the `G` gaps yields

\[
 J\ge {1\over2}\left({S^2\over G}-S\right),
\]

and therefore

\[
 G\ge {S^2\over S+2J}=\Omega_C(rW).
\tag{5.4}

The augmented marker count is `R+G`.  At most two virtual markers were
added per boundary run, for a total of only `O(ke)` virtual markers.  All
actual markers lie in the pairwise disjoint trimmed source spans from
Section 2.  Consequently they are counted at most once in `P(A)`, and
(5.4) proves

\[
 P(A)\ge c_CrW
\]

for some `c_C>0` and all sufficiently large `k`.  This is (0.3).

## 6. Exact scope and what remains open

The theorem removes the normalization premise from the **qualitative**
linear-density barrier.  It proves, for an arbitrary additive-constant
word:

\[
 \boxed{
 \begin{array}{c}
 \text{almost all middle owners lie in literal resident diagonal rows},\\
 \text{their total birth count is }O_C(W),\\
 \text{and their source occurrence mass is }\Omega_C(rW).
 \end{array}}
\tag{6.1}
\]

It does not prove any of the following stronger statements:

1. one complete flat depth-`e` row;
2. Johnson adjacency or exactly one birth per transition;
3. `W+O_C(1)` positive runs;
4. the sharp fixed-carrier density constant
   `4/(16-pi+8C)`;
5. named lower-target compilation from an arbitrary dense occurrence
   schedule;
6. the existence of a universal word of length `B(k)+C`.

The appended-letter example in the additive-`C` scope theorem still
refutes the naive demand for a flat depth-`e` row.  The present diagonal
normalization is the architecture-free replacement: many literal rows,
only `O(e)` raw seams, polynomial trimming loss, `O_C(W)` births, and
positive linear occurrence density.
