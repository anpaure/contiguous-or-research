# Arbitrary-depth suspension of the star compiler obstruction

Date: 2026-07-25

Method: exact mathematics only.

## 0. Outcome

For every fixed \(H\ge2\) and every sufficiently large \(R\), there is a
cyclic rank-\((H+1)\) Johnson walk with \(S=2R\) owners such that

1. at every depth \(0\le q<H\), all consecutive lower intersections are
   pairwise distinct and floor-correct;
2. at depth \(H\), consecutive lower intersections are floor-correct
   singletons, each repeated exactly twice; and
3. every arbitrary nonzero contiguous-OR word covering the lower data
   through depth \(H\) has

\[
 \boxed{L\ge S+\frac{S}{24}.}                     \tag{0.1}
\]

Thus rainbowness through every strictly shallower depth still does not
imply an \(S+O(H)\) compiler at the next depth. The depth-one automatic
facet factorization is genuinely exceptional.

## 1. Base star path

Use distinct coordinates

\[
 b_0,\ldots,b_{R-1},p_0,\ldots,p_{R-1}
\]

with subscripts modulo \(R\). Define a cyclic rank-two Johnson path
\((C_i)_{i\in\mathbb Z_{2R}}\) by

\[
 C_{2t}=\{b_t,b_{t+1}\},
 \qquad
 C_{2t-1}=\{b_t,p_t\}.                             \tag{1.1}
\]

The coordinate \(p_t\) occurs at one base position \(2t-1\), while
\(b_t\) occurs at the three consecutive base positions

\[
 2t-2,\ 2t-1,\ 2t.                                \tag{1.2}
\]

## 2. Window-union suspension

Put

\[
 d=H-1
\]

and, for \(i\in\mathbb Z_{2R}\), define

\[
 Z_i^{(d)}
 =\bigcup_{j=0}^{d}C_{i+j}.                        \tag{2.1}
\]

Assume \(R>2H+2\), so none of the short coordinate intervals below wraps
the whole cycle.

### Lemma 2.1 (exact coordinate runs)

In the owner sequence \((Z_i^{(d)})\),

* \(p_t\) has one positive run of length \(d+1\), from
  \(2t-1-d\) through \(2t-1\);
* \(b_t\) has one positive run of length \(d+3\), from
  \(2t-2-d\) through \(2t\).

At every transition exactly one coordinate enters and one leaves.
Consequently the \(Z_i^{(d)}\) form a cyclic Johnson walk of constant rank

\[
 d+2=H+1.                                         \tag{2.2}
\]

#### Proof

A coordinate belongs to the window union (2.1) exactly when its base
occurrence interval meets \([i,i+d]\). Applying this to the one-position
\(p_t\)-support and the three-position \(b_t\)-support (1.2) gives the two
displayed runs.

The \(p\)-run starts \(2t-1-d\) and the \(b\)-run starts \(2t-2-d\);
together they use every residue modulo \(2R\) once. Their endpoints
\(2t-1,2t\) likewise use every residue once. Hence one coordinate enters
and one leaves at each transition.

Finally, total coordinate residence is

\[
 R(d+1)+R(d+3)=2R(d+2).
\]

Dividing by the \(2R\) owner positions gives rank \(d+2\). \(\square\)

## 3. Every shallower shadow is another suspension

### Lemma 3.1 (exact erosion identity)

For every \(0\le q\le d\),

\[
 \boxed{
 \bigcap_{h=0}^{q}Z_{i+h}^{(d)}
 =Z_{i+q}^{(d-q)}.}                               \tag{3.1}
\]

At depth \(d+1=H\),

\[
 \bigcap_{h=0}^{d+1}Z_{i+h}^{(d)}
\]

is a singleton, and as \(i\) runs around the cycle its value sequence is

\[
 b_0,b_0,b_1,b_1,\ldots,b_{R-1},b_{R-1}
\]

up to cyclic rotation.

#### Proof

Intersecting \(q+1\) consecutive owners erodes every positive coordinate
run by \(q\) positions at its right end. For \(q\le d\), the \(p\)-runs
therefore have length \(d-q+1\), and the \(b\)-runs have length
\(d-q+3\), with the exact shift appearing on the right side of (3.1).
The coordinatewise indicators agree, proving (3.1).

For \(q=d+1\), all \(p\)-runs disappear and every \(b\)-run has length two.
Their starts have one fixed parity and occur every two positions, giving
the displayed repeated-singleton sequence. \(\square\)

For \(0\le e\le d\), the sets \(Z_i^{(e)}\) are pairwise distinct when
\(R>2H+2\). Here is the full parity check.  Write either \(e=2h\) or
\(e=2h+1\).  If \(e=2h\), a window beginning at an odd base position
contains \(h+1\) distinct \(p\)-labels, whereas a window beginning at an
even base position contains only \(h\).  Thus its parity is determined by
its \(p\)-labels, and within either parity their consecutive cyclic block
determines the starting index.  If \(e=2h+1\), then

\[
 \{p:p\in Z_{2t}^{(e)}\}
 =\{p_{t+1},\ldots,p_{t+h+1}\}
 =\{p:p\in Z_{2t+1}^{(e)}\}.                     \tag{3.2}
\]

These are the only two starts that can have the same \(p\)-block, because
its length is less than \(R\).  Their \(b\)-blocks are respectively

\[
 \{b_t,\ldots,b_{t+h+1}\},
 \qquad
 \{b_{t+1},\ldots,b_{t+h+2}\},                  \tag{3.3}
\]

and are different.  This proves pairwise distinctness.  Hence (3.1)
proves injectivity at every depth \(q<H\).
Its rank is

\[
 (H+1)-q,
\]

so every displayed shadow is floor-correct. The depth-\(H\) singletons
are floor-correct as well.

## 4. The hard H1 family reappears in three consecutive depths

At depth \(d=H-1\), identity (3.1) gives the original base owners
\(C_i\), namely the \(X_t,Y_t\) pairs of the H1 star obstruction.

At depth \(d-1=H-2\), it gives

\[
 Z_i^{(1)}=C_i\cup C_{i+1},
\]

namely the upper triples \(U_t^-,U_t^+\) of that obstruction.

At depth \(d+1=H\), Lemma 3.1 gives the lower singletons \(\{b_t\}\).
Therefore the complete depth-\(H\) target family contains exactly the hard
subfamily

\[
 \{b_t\},\quad X_t,Y_t,\quad U_t^-,U_t^+.
\]

The arbitrary-helper canonicalization proof in the H1 obstruction applies
verbatim and yields

\[
 L\ge2R+\frac{R}{12}
   =S+\frac{S}{24}.                                \tag{4.1}
\]

## 5. Fixed-core lift and coefficient-one meaning

Adjoin a fixed core to lift the walk to any larger rank. Projection back
to the active coordinates preserves the lower bound. For rank \(m+1\) in
\([2m+1]\), the needed core has size \(m-H\), and the construction fits
whenever

\[
 2R+(m-H)\le2m+1.
\]

Thus \(S=2R=\Theta(m)\) is available for every fixed \(H\), and also for
slowly growing \(H=o(m)\) after taking \(R\) accordingly.

The theorem is a black-box Johnson obstruction, not a claim about the
canonical PBBS factor. Its exact implication is that no finite list of
shallower rainbow hypotheses can prove the next-depth in-place compiler.
Coefficient one needs a condition acting at all relevant depths
simultaneously—precisely the role of the balanced-shadow, residence-packing,
or global carrier-rethreading gates.
