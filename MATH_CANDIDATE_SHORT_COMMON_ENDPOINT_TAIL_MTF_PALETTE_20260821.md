# Linear-length common-endpoint tail-MTF palettes

**Status (2026-08-21).**  The counting and concatenation theorems below are
proved.  They replace the exponentially long independently bridged blocks by
linear-length fixed-endpoint blocks with exponentially many choices and only
one final polynomial bridge.  They do **not** prove balanced target marginals
or an integral DCC; that is the remaining gate.

## 1. Parameters

Let

\[
n=2m+1,\qquad W={n\choose m},\qquad
H=\left\lceil\sqrt{n\log n}\right\rceil,
\]

and put

\[
K=\{m-H,\ldots,m+1+H\},\qquad
f=m+H+2,\qquad d=n-f+1=m-H.                 \tag{1.1}
\]

A recency state is a permutation of `[n]`.  A legal tail-MTF step moves one
of the positions `f,...,n` to the front, so every state has exactly `d`
outgoing generator choices.  Write `C_k(pi)` for the set in the first `k`
positions of `pi`.  A length-`b` path is **band-simple** when, for every
`k in K`, its `b` post-move sets `C_k` are pairwise distinct.

We use the already proved exact bridge length

\[
R=n^3+f^2,                                             \tag{1.2}
\]

which joins every ordered pair of states by a legal path of exactly `R`
steps.

## 2. Almost every linear word is internally band-simple

Fix an arbitrary initial state `pi` and choose each generator independently
and uniformly from the `d` legal positions.  The history-free return bound
gives, for every `k in K`, every two observation times at gap at least `f`,

\[
\Pr\{C_k(\pi_u)=C_k(\pi_v)\}\le {d!\over d^d};        \tag{2.1}
\]

at a positive gap below `f` the probability is zero.  Consequently, for
every `b>=1`,

\[
\Pr\{\text{the path is not band-simple}\}
 \le \varepsilon_b
 :=|K|{b\choose2}{d!\over d^d}.                       \tag{2.2}
\]

For `b=n`, Stirling's bound and `d=n/2-o(n)` give

\[
\varepsilon_n=\exp\{-n/2+o(n)\}=o(1).                \tag{2.3}
\]

The estimate is uniform in the initial state.

## 3. A rich common endpoint exists after exactly `n` steps

For states `pi,eta`, let `G(pi,eta)` be the set of band-simple legal
generator words of length exactly `n` that take `pi` to `eta`.

### Theorem 3.1 (linear common-endpoint bundle)

For every initial state `pi`, some endpoint `eta` satisfies

\[
|G(\pi,\eta)|
 \ge {(1-\varepsilon_n)d^n\over n!}
 =\exp\{(1-\log2)n+o(n)\}.                            \tag{3.1}
\]

In particular, every state has a length-`n` common-endpoint bundle with
exponentially many internally band-simple options.

#### Proof

There are `d^n` legal generator words of length `n`.  By (2.2), at least
`(1-epsilon_n)d^n` are band-simple.  They end at at most `n!` states, so one
endpoint receives at least their average number.  Finally,

\[
\log {d^n\over n!}
 =n\log d-\log(n!)
 =(1-\log2)n+o(n),                                    \tag{3.2}
\]

because `d/n=1/2-o(1)` and
`log(n!)=n log n-n+o(n)`.  This proves (3.1).  \(\square\)

There are also many reachable endpoints, even without a mixing theorem.
For fixed initial and terminal states, the ordered last-`f` emitted-letter
suffix is forced: it is the reverse of the terminal state's first `f`
letters.  After the first `n-f` generator positions have been fixed, the
intermediate state is fixed, and this forced letter suffix determines at
most one legal generator-position suffix.  Hence an endpoint fiber of length
`n` has size at most `d^(n-f)`, and (2.2) also gives

\[
|\{\eta:G(\pi,\eta)\ne\varnothing\}|
 \ge(1-\varepsilon_n)d^f.                             \tag{3.3}
\]

This endpoint abundance will matter if one tries to balance successive
bundles rather than always choosing a largest fiber.

## 4. A full near-`W` palette with only one bridge

Choose an arbitrary state `gamma_1`.  Starting from `gamma_i`, apply Theorem
3.1 and fix one rich endpoint `gamma_(i+1)`.  This recursively defines a
fixed skeleton and, in slot `i`, the option set

\[
\mathcal G_i=G(\gamma_i,\gamma_{i+1}).                \tag{4.1}
\]

Put

\[
s=\left\lfloor{W-R\over n}\right\rfloor,
\qquad N=sn.                                          \tag{4.2}
\]

Select one path from each `mathcal G_i`, concatenate the selected paths, and
append one exact `R`-step
bridge from `gamma_(s+1)` back to `gamma_1`.

### Theorem 4.1 (short-block closed palette)

For all sufficiently large odd `n`, the construction above has the following
properties.

1. Every slot has at least
   `exp((1-log 2)n+o(n))` band-simple fixed-endpoint options.
2. Every choice of one option per slot concatenates legally without an
   inter-slot connector.
3. The final word is a closed legal tail-MTF trajectory of length

   \[
   L=sn+R\le W,\qquad W-N=O(R+n)=o(W).                \tag{4.3}
   \]

4. Periodic repetition of the operator word is legal, so equal letters have
   cyclic gap at least `f`.  Every one of the `N` core observations is clean
   throughout the DCC band, and each individual slot has no within-slot
   target repetition at any band rank.

#### Proof

Item 1 is Theorem 3.1 at each recursively fixed start state.  All paths in
slot `i` have the same prescribed terminal state `gamma_(i+1)`, which is the
prescribed initial state of slot `i+1`; hence item 2.  The one final bridge
closes the state trajectory.  Equation (4.2) gives `L<=W` and
`0<=W-N<R+n`; since `R=O(n^3)` and `W` is exponential, (4.3) follows.
Every step in the closed trajectory is legal.  Repeating the same closed
operator word is therefore legal across the cyclic seam, which enforces the
gap floor.  Band-simplicity gives the final assertion inside each core.
\(\square\)

The uncontrolled observations are now only the single `R`-step closing
bridge, rather than `2sR` connector observations.  Cross-slot target
collisions can still be linear and are **not** bounded by Theorem 4.1.

## 5. What this changes, and what it does not

The independently bridged palette used core length `a=exp(n/5)` in order to
make `sR=o(W)`.  Theorem 4.1 has block length exactly `n`,

\[
s=(1+o(1)){W\over n},qquad
\text{raw band incidence per block}=n|K|
 =O(n^{3/2}\sqrt{\log n}),                            \tag{5.1}
\]

and still has exponentially many options per slot.  Thus connector cost no
longer forces enormous bundle rank.  This removes one quantitative obstacle
to a custom parity/graphic nibble.

What is missing is just as important.  The endpoint chosen by pigeonhole need
not give a relabeling-invariant option law.  The theorem therefore proves no
uniform target degrees, no fractional perfect matching, no retained-parity
packing, and no control of cross-slot cyclomatic rank.  The next useful
statement would be either

1. a way to choose the abundant endpoint skeleton (3.3) so that the
   resulting short palettes have total target-marginal defect `o(W)`, or
2. a direct integral selection from these short bundles whose retained
   parity has `o(W)` collision/leave and whose omitted-parity deck union has
   `o(W)` cyclomatic rank.

Either would feed the exact parity/graphic reduction.  Theorem 4.1 by itself
does not prove `nu(n)=(1+o(1))W`.
