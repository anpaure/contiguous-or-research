# All four MNW suffix currents are q2-support-neutral

**Date:** 2026-08-07  
**Method:** exact symbolic turn calculation and the canonical MSW inverse
test; no computation or search  
**Status:** unconditional no-support theorem for every suffix-tensored
single MNW tuple.  The four base tuple types \(\alpha,\beta,\gamma,\delta\)
can change q2 multiplicities, but every q2 target they introduce is already
in the canonical q2 image.  Consequently a missing target can first appear
only at a compound centre whose two incident canonical edges are both
rethreaded (or through a nonsuffix context not covered by this theorem).

## 1. Signed q2 current

Let \(P(x)\) be one canonical MSW incidence path, and remove its complement
closure edge.  At an internal rank-\(m\) vertex \(X\), let its two
rank-\((m+1)\) neighbours be \(U^-(X),U^+(X)\).  Its q2 turn is

\[
                         \Gamma(X)=U^-(X)\cup U^+(X).
\]

For one flipping tuple \(\phi\), toggle its witnessing cycle while leaving
all other factor edges canonical.  Define the signed q2 current

\[
 \partial_2\phi
 =\sum_{X\text{ changed internal centre}}[Gamma_{\rm new}(X)]
  -\sum_{X\text{ changed internal centre}}[Gamma_{\rm old}(X)].
                                                               \tag{1.1}
\]

Endpoint rank-\(m\) vertices are omitted because they have degree one after
the complement closure matching is removed and carry no q2 turn.

If \(v\) is a Dyck word appended to every path root and every vertex of a
flipping cycle, the MSW concatenation identity appends the same \(v\) to
every old and new turn.  Thus it suffices to calculate the four base
currents and then append \(v\).

## 2. The alpha current

For a Dyck word \(w\), the flipping cycle is

\[
 \begin{aligned}
 1w00101,&\ 1w00111,\ 1w00110,\ 1w10110,\\
         &\ 1w10100,\ 1w10101.
 \end{aligned}                                      \tag{2.1}
\]

The third supported path starts

\[
 1w10010,\ 1w10110,\ 1w00110,\ 1w01110,\ldots.     \tag{2.2}
\]

The last displayed step follows directly from the MSW recursion: in the
first-return decomposition of \(1w10010\), the mirrored inner word is
\(10\overleftrightarrow w\), whose first two flip positions are \(2,1\).

There are two internal changed centres.  Their turn ledger is

\[
 \begin{array}{c|c|c}
 \text{centre}&\text{old turn}&\text{new turn}\\ \hline
 1w00101&1w01111&1w11101\\
 1w00110&1w11110&1w01111.
 \end{array}                                        \tag{2.3}
\]

Therefore, after appending an arbitrary Dyck suffix \(v\),

\[
 \boxed{
 \partial_2(\alpha(w)v)
 =[1w11101v]-[1w11110v].}                           \tag{2.4}
\]

## 3. The beta, gamma and delta currents

The complete internal-centre ledgers are as follows.

### Beta

\[
 \begin{array}{c|c|c}
 \text{centre}&\text{old turn}&\text{new turn}\\ \hline
 011001&011111&111101\\
 011010&111110&011111.
 \end{array}
\]

Hence

\[
 \boxed{
 \partial_2(\beta v)=[111101v]-[111110v].}          \tag{3.1}
\]

### Gamma

\[
 \begin{array}{c|c|c}
 \text{centre}&\text{old turn}&\text{new turn}\\ \hline
 10011100&11111100&10111101\\
 10011001&10111101&11111001.
 \end{array}
\]

Hence

\[
 \boxed{
 \partial_2(\gamma v)=[11111001v]-[11111100v].}     \tag{3.2}
\]

### Delta

\[
 \begin{array}{c|c|c}
 \text{centre}&\text{old turn}&\text{new turn}\\ \hline
 110001&110111&111101\\
 011010&111110&011111.
 \end{array}
\]

Hence

\[
 \boxed{
 \partial_2(\delta v)
 =[111101v]+[011111v]-[110111v]-[111110v].}          \tag{3.3}
\]

These identities use only the explicit MNW paths and the four witnessing
cycles.  Repeated terms in the two local rows have been cancelled in
(2.4), (3.1), and (3.2).

## 4. Every positive term is canonically present

Use the exact canonical inverse criterion for an endpoint-height-four
target \(T\).  It asks for up-step positions \(p<q\) with starting heights
\(0\) or \(1\) at \(p\), starting heights \(2\) or \(3\) at \(q\), no
intervening down-step starting at height two or three, and equal left/right
ordinal counts.

### Lemma 4.1

Every positive term in (2.4), (3.1)--(3.3) belongs to the canonical MSW q2
image, for every displayed Dyck \(w,v\).

#### Proof

For

\[
 T=1w11101v,
\]

choose \(p\) to be the first up-step of the final block \(11101\) and
\(q\) its third up-step.  They start at heights one and three.  The only
step strictly between them is an up-step from height two.  Before \(p\),
the initial first bit is the unique height-zero up-step; the Dyck word
\(w\), read from height one, contributes none.  After \(q\), the final
up-step of \(11101\) is the unique height-three up-step; the suffix \(v\),
read from height four, contributes none.  Both ordinal counts are one.
This proves canonical presence of the alpha gain, and includes the beta
gain when \(w\) is empty.

For

\[
 T=11111001v,
\]

take \(p=2\), \(q=4\).  Their starting heights are one and three; the
intervening position is an up-step from height two.  The height-zero
up-step before \(p\) is position one, and the height-three up-step after
\(q\) is position eight.  Again both counts are one and \(v\) begins at
height four.  This proves canonical presence of the gamma gain.

Finally, for

\[
 T=011111v,
\]

take \(p=3\), \(q=6\).  Their starting heights are zero and three, every
intervening step is up, and both ordinal counts are zero.  The suffix
again starts at height four.  This proves canonical presence of the second
delta gain. \(\square\)

### Theorem 4.2 (suffix-tensor single-tuple no-support theorem)

Let \(\mathcal U\) be any family of suffix-tensored MNW tuples of the four
types above whose canonical path supports are pairwise disjoint.  Apply all
their flipping cycles to the canonical factor.  No canonically missing q2
target becomes represented.

#### Proof

Disjoint path supports imply that no rank-\(m\) centre is touched by two
tuples.  Thus the total current is the sum of the isolated currents
(2.4), (3.1)--(3.3).  Lemma 4.1 says every new target was already
canonically represented.  Removing old occurrences can preserve or shrink
the support, but cannot add a formerly missing target. \(\square\)

The theorem applies in particular to the pairwise-disjoint bank
\(\{\alpha(\varnothing)v:v\in\mathcal D_{m-3}\}\).  Its Catalan size is
therefore multiplicity mobility, not missing-target repair capacity.

## 5. Exact compound-centre criterion

Let \(X\) be an internal rank-\(m\) vertex on one canonical path.  Write its
two canonical facets as

\[
                         X+a,\qquad X+b,              \tag{5.1}
\]

where \(a,b\notin X\) are distinct.  Suppose two selected tuples remove
the two corresponding canonical edges and replace them by the cross facets

\[
                         X+c,\qquad X+d.              \tag{5.2}
\]

The marks of the two tuples are the two consecutive flip coordinates
around \(X\).  They are distinct, as required by MNW conflict-freeness.

### Theorem 5.1 (compound repair identity)

The final q2 turn at \(X\) is

\[
                         \boxed{X\cup\{c,d\}}.        \tag{5.3}
\]

Consequently a missing target \(R\in\binom\Omega{m+2}\) is created at
\(X\) if and only if

\[
 X\subset R,
 \qquad \{c,d\}=R\setminus X,                        \tag{5.4}
\]

and the two marked tuples realizing (5.2) coexist in the selected
conflict-free spanning hypertree.

#### Proof

Both new facets contain \(X\), so their union is

\[
 (X+c)\cup(X+d)=X\cup\{c,d\}.
\]

They are distinct neighbours in a simple incidence factor, so \(c\ne d\).
This gives rank \(m+2\) and proves (5.3).  Equality with \(R\) is exactly
(5.4). \(\square\)

### Definition 5.2 (compound repair graph)

For every canonical centre \(X\), let \(e_X^-,e_X^+\) be its two incident
path edges.  A **compound offer** is an ordered pair of MNW tuples
\((\tau^-,\tau^+)\) such that

1. \(\tau^-\) is marked at \(e_X^-\) and installs \(X+c\);
2. \(\tau^+\) is marked at \(e_X^+\) and installs \(X+d\);
3. their supports meet in at most \(X\)'s canonical path root; and
4. \(c\ne d\).

Join the offer to target \(R\) exactly when (5.4) holds.  A support repair
inside the MNW language now requires a target-covering selection of
compound offers that extends to one conflict-free spanning hypertree.

This is the exact next Hall/topology gate.  Ordinary abundance of isolated
tuples, including the full Catalan alpha bank, is irrelevant to it.

## 6. Scope

The theorem proves a no-support statement for suffix-tensored isolated
tuples.  It does not yet classify:

1. arbitrary nonempty-prefix or mirrored contexts from the full MNW
   language;
2. which compound offers of Definition 5.2 actually exist;
3. whether they cover the canonical missing family;
4. whether a covering selection extends to a spanning hypertree; or
5. compatibility with global residence and the literal compiler.

The immediate target is therefore not another count of MNW flips.  It is
the existence and Hall expansion of the compound repair graph.

