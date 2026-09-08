# Bottom Boolean stars: the small-junta container claim is false

**Date:** 2026-08-05  
**Method:** exact adjacent-shadow algebra, moderate-deviation estimates for
the hypergeometric law, and simultaneous hypergeometric concentration; no
computation or search  
**Status:** rigorous obstruction and corrected positive theorem.  Independent
uniform samples are not refuted.  What is refuted is the proposed structural
route saying that every near-tight Boolean-star Hall cut is approximable by an
`O(sqrt(m))`-coordinate junta.  There are closed, 2-linked, near-tight cuts
depending essentially on `Theta(m)` coordinates.  They are nevertheless easy
to balance because their whole catalogue has entropy only `O(m)`.  Thus the
right replacement is a drift-sensitive **entropy container** theorem, not a
small-coordinate-junta theorem.

## 1. The independently sampled middle-level model

Put

\[
 n=2m-1,\qquad
 \mathcal L={ [n]\choose m-1},\qquad
 \mathcal R={ [n]\choose m},\qquad
 W=|\mathcal L|=|\mathcal R|.
 \tag{1.1}
\]

Let `X_-` and `X_+` be independent uniform `H`-subsets of `mathcal L` and
`mathcal R`, respectively, where

\[
                         H=\Theta(W/\sqrt m).               \tag{1.2}
\]

The induced Boolean-star graph has matching deficiency

\[
 \operatorname{def}(X_-,X_+)
 =\max_{A\subseteq X_+}
       \bigl(|A|-|N(A)\cap X_-|\bigr).
 \tag{1.3}
\]

Equivalently, by extending `A` to its closure if necessary, its cuts are
described by closed families `A subseteq mathcal R` and their lower shadows
`N(A) subseteq mathcal L`.

The desired independent-sampling theorem is

\[
                         \operatorname{def}(X_-,X_+)=O(H/m). \tag{1.4}
\]

The construction below does **not** contradict (1.4).  It contradicts the
suggested intermediate assertion that every cut relevant at this scale has an
`O(sqrt(m))`-coordinate container.

## 2. A half-coordinate threshold cut

Fix `J subseteq [n]` with `|J|=m`.  If `T` is uniform in `mathcal R`, put

\[
                         Z=|T\cap J|.                        \tag{2.1}
\]

This is hypergeometric with parameters `(2m-1,m,m)`.  Its variance is

\[
 \sigma_m^2
 =m{m\over2m-1}{m-1\over2m-1}{m-1\over2m-2}
 ={m\over8}+O(1).                                           \tag{2.2}
\]

The uniform local central limit theorem for the hypergeometric distribution
implies that there is an integer `a=a_m` satisfying

\[
 {\mathbb P}(Z=a+1)=\Theta(1/m),\qquad
 {\mathbb P}(Z\le a)=\Theta\!\left({1\over\sqrt{m\log m}}\right).
 \tag{2.3}
\]

For example, one may take

\[
 a=\left\lfloor {m^2\over2m-1}-\sigma_m\sqrt{\log m}\right\rfloor
 \tag{2.4}
\]

and change it by at most one.  Stirling's formula, uniformly in the
moderate-deviation range `|a-EZ|=O(sqrt(m log m))`, gives (2.3) directly.

Define

\[
 \mathcal A(J,a)=\{T\in\mathcal R:|T\cap J|\le a\},
 \qquad
 \mathcal C(J,a)=\{K\in\mathcal L:|K\cap J|\le a\}.
 \tag{2.5}
\]

### Lemma 2.1 (exact shadow)

For `1<=a<=m-2`,

\[
                         N(\mathcal A(J,a))=\mathcal C(J,a). \tag{2.6}
\]

#### Proof

If `K subset T` and `T in mathcal A(J,a)`, then `|K cap J|<=a`, so the
left side is contained in the right side.

Conversely, let `K in mathcal C(J,a)`.  If `|K cap J|<a`, any unused
coordinate can be added unless it is preferable to add outside `J`.  If
`|K cap J|=a`, add an unused coordinate outside `J`.  Such a coordinate
exists: otherwise `K` contains all `m-1` coordinates outside `J`, forcing
`|K cap J|=0`, contrary to the present central range.  The resulting
`T=K+x` belongs to `mathcal A(J,a)`.  This proves (2.6).  \(\square\)

Thus

\[
 \mathcal A(J,a)\ \dot\cup\
 \bigl(\mathcal L\setminus\mathcal C(J,a)\bigr)             \tag{2.7}
\]

is an empty rectangle, or equivalently an independent set in the two middle
layers.

### Lemma 2.2 (exact adjacent-layer drift)

Let

\[
 t(J,a)=|\mathcal C(J,a)|-|\mathcal A(J,a)|.                \tag{2.8}
\]

Then

\[
 {t(J,a)\over W}
 ={a+1\over m}\,{\mathbb P}(Z=a+1).                        \tag{2.9}
\]

In particular, for the choice (2.3),

\[
                         t(J,a)=\Theta(W/m).                \tag{2.10}
\]

#### Proof

Couple a uniform `T in mathcal R` to a uniform `K in mathcal L` by deleting
a uniformly random `x in T`.  The event `K in mathcal C(J,a)` but
`T notin mathcal A(J,a)` occurs exactly when `Z=a+1` and the deleted
coordinate lies in `J`.  Conditional on `Z=a+1`, this has probability
`(a+1)/m`.  This proves (2.9), and (2.3) gives (2.10).  \(\square\)

### Lemma 2.3 (closed and 2-linked)

The family `mathcal A(J,a)` is closed in the Boolean-star graph and is
2-linked.

#### Proof

By Lemma 2.1 its shadow is `mathcal C(J,a)`.  If `T notin mathcal A(J,a)`,
then `|T cap J|>=a+1`.  When equality holds, removing a coordinate outside
`J` leaves a lower set with `a+1` coordinates of `J`, which is outside
`mathcal C(J,a)`; such an outside coordinate exists in the range (2.3).
When `|T cap J|>a+1`, every appropriate lower facet is already outside.
Thus `N(T)` is not contained in `mathcal C(J,a)`, proving closure.

The Johnson graph induced by the condition `|T cap J|<=a` is connected:
one may transform any member to a fixed canonical member by swaps, first
decreasing `|T cap J|` when necessary and then permuting within `J` and its
complement without ever increasing it past `a`.  Johnson adjacency is
distance two in the incidence graph, so the family is 2-linked. \(\square\)

## 3. No `O(sqrt(m))`-coordinate junta approximates the cut

### Theorem 3.1 (small-junta obstruction)

Fix `C>0`.  For the family in (2.5), uniformly over every coordinate set
`S subseteq[n]` with `|S|<=C sqrt(m)` and every Boolean function
`g:2^S->{0,1}`,

\[
 \left|
 \mathcal A(J,a)\,\triangle\,
 \{T\in\mathcal R:g(T\cap S)=1\}
 \right|
 \ge (1-o(1))|\mathcal A(J,a)|
 =\Theta\!\left({W\over\sqrt{m\log m}}\right).             \tag{3.1}
\]

In particular this error is `omega(W/m)`.  Hence a deterministic theorem
which replaces every closed near-tight cut by an `O(sqrt(m))`-coordinate
junta with `O(W/m)` error is false.

#### Proof

Condition on an arbitrary pattern `T cap S=P`.  The remaining value of
`|T cap J|` is again hypergeometric, now on `2m-1-|S|` coordinates.  Its
variance is `Theta(m)` uniformly over every feasible pattern.  Conditioning
on at most `C sqrt(m)` coordinates shifts its mean by at most `O(sqrt(m))`.
The threshold in (2.4) remains a negative moderate deviation of order
`sqrt(log m)` standard deviations, up to an additive `O(1)` in the
standardized coordinate.

The hypergeometric Chernoff bound (or the same uniform Stirling estimate as
in (2.3)) therefore gives, uniformly in every feasible `P`,

\[
 \Pr(T\in\mathcal A(J,a)\mid T\cap S=P)
 \le m^{-1/2+o(1)}<1/2.                                   \tag{3.2}
\]

Thus the Bayes-optimal prediction from `T cap S` is identically zero: on
every fibre, changing the predicted value from zero to one increases the
classification error.  Consequently every `S`-junta has error at least the
error of the zero function, namely `|mathcal A(J,a)|`, up to the harmless
`o(1)` uniformity loss in (3.2).  Equation (2.3) gives the last equality in
(3.1).  \(\square\)

The example is at precisely the scale relevant to the proposed theorem:
its deterministic adjacent-layer expansion is `Theta(W/m)`, not a much
larger expansion which could simply be discarded before the fine Hall
analysis.

## 4. Why this is not a counterexample to independent sampling

The threshold cuts form a very small catalogue:

\[
 \mathfrak T
 =\{(\mathcal A(J,a),\mathcal C(J,a)):
       J\subseteq[n],\ -1\le a\le |J|\},
 \qquad
 |\mathfrak T|\le (n+2)2^n.                               \tag{4.1}
\]

### Theorem 4.1 (all threshold cuts balance at the sharp scale)

Let `X_-` and `X_+` be the independent uniform samples of size `H` in
(1.2).  With probability

\[
 1-4(n+2)2^n\exp\!\left(-{2H\over m^2}\right)=1-o(1),     \tag{4.2}
\]

simultaneously for every `(J,a)`,

\[
 |X_+\cap\mathcal A(J,a)|
 -|X_-\cap\mathcal C(J,a)|
 \le {2H\over m}.                                         \tag{4.3}
\]

#### Proof

For either slice and any fixed event, sampling without replacement and
Hoeffding's inequality give

\[
 \Pr\left(left||X_\pm\cap E|-H{|E|\over W}\right|>{H\over m}\right)
 \le2\exp\!\left(-{2H\over m^2}\right).                  \tag{4.4}
\]

Union-bound over two shores and the catalogue (4.1).  Since
`log H=Theta(m)`, the error in (4.2) tends to zero.  On the resulting event,
Lemma 2.2 gives

\[
 \begin{aligned}
 |X_+\cap\mathcal A|-|X_-\cap\mathcal C|
 &\le H{|\mathcal A|-|\mathcal C|\over W}+{2H\over m}\\
 &\le {2H\over m},
 \end{aligned}                                             \tag{4.5}
\]

which proves (4.3). \(\square\)

Thus the counterexample family is harmless for independent samples for a
reason quite different from small-coordinate structure: it has low
**catalogue entropy**.

## 5. Audit of the simultaneous junta-balance theorem

The theorem in

`MATH_THEOREM_SIMULTANEOUS_JUNTA_BALANCE_ADJACENT_MIDDLE_LAYERS_20260805.md`

is correct as stated.

* The deletion coupling gives total-variation distance at most `|J|/n`.
* Balancing every pattern cell to `epsilon/2^t` gives total variation at
  most `epsilon/2` on each empirical shore.
* The count of pairs `(J,P)` with `|J|<=t` is bounded by
  `2^t(en/t)^t`; the two shores and two Hoeffding tails account for the
  factor four in its hypothesis.
* For `t=O(sqrt n)`, `H=Theta(W/sqrt n)`, and `epsilon=1/n`, its numerical
  condition holds by an exponential margin.

Its conditional corollary, however, cannot be fed by a blanket assertion
that all near-tight cuts have `O(sqrt m)` coordinate support: Theorem 3.1
disproves that assertion.

## 6. Correct replacement target

The proof-safe structural target is a **drift-sensitive entropy-container
theorem**.

For every closed, 2-linked `A` with `|A|<=W/2`, put

\[
                         t(A)=|N(A)|-|A|.                  \tag{6.1}
\]

It would suffice to produce paired approximants `(S,F)` such that:

1. `A subseteq S` and `F subseteq N(A)`;
2. the approximation error is charged to `O(t(A))` literal vertices;
3. at every fixed drift scale `t`, the logarithm of the number of possible
   paired approximants is small compared with the hypergeometric deviation
   exponent at that scale; and
4. special high-complexity but low-entropy classes, such as the threshold
   cuts above, are retained as whole containers rather than forced into
   coordinate juntas.

The usual Sapozhenko fingerprint/approximation pair is the natural starting
point, but its entropy has to be compared scale-by-scale with

\[
 \Pr\bigl(
 |X_+\cap A|-|X_-\cap N(A)|\ge H/m
 \bigr),                                                    \tag{6.2}
\]

not replaced by coordinate width alone.

## 7. Verdict on the independent-uniform theorem

No independent-uniform counterexample is produced here.  The sharp
threshold family that defeats the proposed junta classification satisfies
the desired `O(H/m)` empirical Hall bound simultaneously over all its
coordinate choices.

Accordingly, the present proof status is:

\[
 \boxed{
 \begin{array}{l}
 \text{small-coordinate structural container: false;}\\
 \text{all threshold/cumulative-coordinate cuts: balanced at }O(H/m);\\
 \text{arbitrary independent-uniform Boolean-star deficiency: still open.}
 \end{array}}
 \tag{7.1}
\]

The next mathematical step is not a Kruskal--Katona-to-junta theorem.  It is
a scale-sensitive Sapozhenko entropy theorem, with the moderate-deviation
threshold families admitted as legitimate high-coordinate containers.

