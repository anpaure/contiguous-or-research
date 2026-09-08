# The common-core collision functional under two-base conveyors: exact derivative and an isolated high-energy state

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad
 L=m-3H+1,\qquad
 N=\binom{2m}{m-H},\qquad
 W=\binom{2m}{m},
\tag{0.1}
\]

and let a labelled common-core state choose one length-\(L\) path at
every rank-\(M\) top.  If \(K_D\) is the resulting middle-owner load,
write

\[
                    \Psi(K)=\sum_{D\in\binom{[2m]}m}\binom{K_D}{2}.
\tag{0.2}
\]

This note determines exactly what the three-top/two-base conveyor of
`MATH_THEOREM_THREE_TOP_TWO_BASE_PROMOTION_CONVEYOR_20260726.md` and its
symmetric six-frame version can do to \(\Psi\).

1.  For every common phase restriction for which the old and new
    packet shores are coordinate-conjugate, if their middle incidence
    vectors are \(\Gamma^0,\Gamma^1\), \(\Delta=\Gamma^1-\Gamma^0\),
    and \(R\) is the load outside the packet, then

    \[
       \boxed{\Psi(R+\Gamma^1)-\Psi(R+\Gamma^0)
                    =\langle R,\Delta\rangle.}
    \tag{0.3}
    \]

    Thus there is no intrinsic restitution term.  This is the exact
    local-optimum criterion, not merely a sufficient inequality.

2.  For the complete middle decks, and for every protected/inert-hole
    suspension proved in the cited conveyor theorem,

    \[
                         \Gamma^1=\Gamma^0.
    \tag{0.4}
    \]

    Consequently these exchanges preserve \(\Psi\) against every
    exterior.  They provide no descent direction at all for the
    common-core middle coefficient energy.

3.  This flatness is not the only obstruction to a local-descent
    theorem.  There is an explicit labelled common-core state
    \(\mathcal S_\sigma\), obtained by restricting one master cyclic
    order to every top, which contains no shore of any distinct-top
    two-base conveyor having a path of at least two edges.  It therefore
    contains neither the three-top conveyor nor its six-frame
    realization.  The same argument excludes the six-frame
    mixed-spectator cycle primitive.

    Nevertheless, if

    \[
                       T=LN=\rho W,
    \tag{0.5}
    \]

    then

    \[
       \boxed{
       \Psi(\mathcal S_\sigma)
       \ge \left({\rho^2 2^H\over4m}-{\rho\over2}\right)W.}
    \tag{0.6}
    \]

    In the calibrated regime \(\rho=1-o(1)\) and
    \(H=(1+o(1))\sqrt{m\log m}\), this is much larger than \(W\).
    Hence \(\mathcal S_\sigma\) is an isolated, high-energy local
    minimum for this labelled move catalogue.

The conclusion is a no-go for a descent proof based only on locating
one of these finite conveyors in the current labelled state.  It is not
a lower bound on \(\min\Psi\): a larger move, or a sequence using
zero-energy changes of labelled representation before a conveyor, is
not excluded.

## 1. Universal packet derivative

Let \(\mathcal D=\binom{[2m]}m\).  Suppose a packet changes the selected
paths at a fixed set of tops.  Let

\[
             \Gamma^j\in\mathbb Z_{\ge0}^{\mathcal D}
             \qquad(j=0,1)
\tag{1.1}
\]

be the aggregate middle incidence vectors on its two shores.  Both
shores have the same number of paths of the same length, so

\[
       \sum_D\Gamma_D^0=\sum_D\Gamma_D^1.
\tag{1.2}
\]

### Lemma 1.1 (exact collision derivative)

For \(\Delta=\Gamma^1-\Gamma^0\) and every fixed exterior load \(R\),

\[
\begin{aligned}
 \Psi(R+\Gamma^1)-\Psi(R+\Gamma^0)
 ={}&\langle R,\Delta\rangle
   +\frac12\bigl(\|\Gamma^1\|_2^2-\|\Gamma^0\|_2^2\bigr).
\end{aligned}
\tag{1.3}
\]

#### Proof

Use

\[
                    \Psi(X)={1\over2}
                    \left(\|X\|_2^2-\sum_DX_D\right).
\tag{1.4}
\]

The linear terms cancel by (1.2).  Expanding the two squared norms
gives (1.3). \(\square\)

### Theorem 1.2 (toll-free derivative of every conjugate conveyor)

Take either the three-top/two-base conveyor or the symmetric six-frame
conveyor.  Retain any common set of positional phases on all touched
frames, provided this gives valid common-core paths.  Then the label
involution displayed in the cited theorems sends the old packet shore
to the new shore without changing the retained phase set.  Therefore

\[
                         \|\Gamma^1\|_2=\|\Gamma^0\|_2,
\tag{1.5}
\]

and (0.3) holds.

In particular, a state containing the old shore is locally minimizing
against this one alternative exactly when

\[
                \boxed{\langle R,\Gamma^1-\Gamma^0\rangle\ge0.}
\tag{1.6}
\]

#### Proof

For the three-top packet, the involution is

\[
                         x\longleftrightarrow y,
                         \qquad a\longmapsto a,
\tag{1.7}
\]

with the common core fixed.  It fixes the direct top and interchanges
the two path-edge tops.  It maps every retained old phase to the
corresponding retained new phase.  Thus it acts as a permutation of
the target coordinates and maps \(\Gamma^0\) to \(\Gamma^1\), proving
(1.5).  The six-frame involution additionally reverses each of the two
three-edge paths and has the same conclusion.  Lemma 1.1 now gives
(0.3), and (1.6) is simply its nonnegativity criterion. \(\square\)

No assertion that the scalar product in (1.6) has a favorable sign is
implicit in the construction.

### Corollary 1.3 (complete local-optimum characterization)

In the labelled state graph generated by coordinate-conjugate
three-top and six-frame conveyor replacements, a state \(K\) is a
local minimum of \(\Psi\) if and only if, for every packet shore
\(\Gamma^0\) occurring in the state and its legal mate \(\Gamma^1\),

\[
       \left\langle K-\Gamma^0,\Gamma^1-\Gamma^0\right\rangle\ge0.
\tag{1.8}
\]

#### Proof

The exterior load for that replacement is exactly
\(R=K-\Gamma^0\).  Apply Theorem 1.2 to every incident move. \(\square\)

## 2. Exact flatness of the proved middle-preserving suspensions

### Theorem 2.1 (middle fibre flatness)

For the complete three-top or six-frame conveyor at the middle layer,
the two aggregate incidence vectors are identical.  The same is true
after deleting any collection of phases whose individual packet
derivatives vanish, including the protected deletions proved in the
six-frame theorem.  Consequently

\[
                    \Psi(R+\Gamma^1)=\Psi(R+\Gamma^0)
\tag{2.1}
\]

for every exterior \(R\).

#### Proof

For a positional base \(\theta\), let
\(d_H(\theta;x,y)\) be its complete radius-\(H\) placeholder-swap
derivative.  The two bases satisfy

\[
                         d_H(\omega';x,y)
                         =-d_H(\omega;x,y).
\tag{2.2}
\]

The endpoint telescope on either the three-top or six-frame shore gives

\[
                         \Gamma^1-\Gamma^0
                         =d_H(\omega;x,y)
                          +d_H(\omega';x,y)=0.
\tag{2.3}
\]

Complementation from omitted \(H\)-windows to physical middle owners is
a coordinate bijection, so (2.3) is the literal physical load identity
\(\Gamma^1=\Gamma^0\).  A phase with zero packet derivative contributes
zero to both sides of (2.3), so deleting any collection of such phases
preserves the identity.  Equation (2.1) follows immediately. \(\square\)

This theorem is stronger than equality of intrinsic norms.  It says
that the move lies entirely inside one middle-load fibre.  In
particular, the identity

\[
              \Phi_{\rm cc}=\Psi+(W-LN)
\tag{2.4}
\]

shows that the same move is exactly flat for \(\Phi_{\rm cc}\).

An arbitrary non-inert truncation must not be folded into Theorem 2.1:
it can have \(\Delta\ne0\).  Its exact derivative is (0.3), and no sign
has been proved.

### Proposition 2.2 (an actual length-\(L\) inert suspension)

Assume \(m\ge10H-4\).  The filler blocks in the two-base construction
can be chosen so that Theorem 2.1 has a common-core realization with
exactly \(L=m-3H+1\) retained phases.  In particular, the flat move
does occur inside the all-core path catalogue, rather than only in the
complete-frame catalogue.

#### Proof

Put the whole filler of size

\[
                         M-8H+2
\tag{2.5}
\]

into \(F_1\).  The common placeholder-free segment

\[
             \widehat A^+,F_1,\overleftarrow{\widehat B^-}
\tag{2.6}
\]

then has length

\[
                         M-6H+2=m-5H+2.
\tag{2.7}
\]

Delete \(4H-1\) consecutive phases whose middle omitted
\(H\)-windows lie in this segment.  The union of those consecutive
windows has length

\[
                         (4H-1)+(H-1)=5H-2,
\tag{2.8}
\]

which fits by the assumed inequality.  Every deleted phase contains
neither placeholder and hence has zero packet derivative.  Exactly

\[
                         M-(4H-1)=m-3H+1=L
\tag{2.9}
\]

consecutive phases remain.

Their \(H\)-omission windows form a tight path whose underlying
injective word has length \(L+H-1=m-2H\).  Its complement in the top
has size \(3H\); choosing any \(2H\) of those complementary labels as
the protected core realizes the path in the full all-core catalogue.
Theorem 2.1 supplies its exact flatness. \(\square\)

## 3. A master-order common-core state

Fix a directed cyclic order \(\sigma\) on \([2m]\) and distinguish a
cut, so that its restrictions can be read linearly.  For every
rank-\(M\) top \(U\), list its elements in the induced order

\[
                         \sigma|_U=(u_1,\ldots,u_M).
\tag{3.1}
\]

Take

\[
 Q_U=\{u_1,\ldots,u_{2H}\},
 \qquad
 S_U=(u_{2H+1},\ldots,u_M).
\tag{3.2}
\]

Use these two blocks, in the displayed order, in the common-core path
construction.  Since \(|S_U|=m-H\), its retained middle omissions are
the \(L\) consecutive \(H\)-windows of one injective subword of
\(\sigma|_U\).  This gives one valid labelled option at every top; call
the product state \(\mathcal S_\sigma\).

### Lemma 3.1 (restriction consistency forbids a two-edge conveyor)

Let \(C\) be fixed and let \(A,B\) be two distinct positional gaps of a
cyclic order on \(C\), separated by at least one core label.  There do
not exist distinct labels \(x,a,y\notin C\) for which both cyclic orders

\[
        \theta^+(x,a)\quad\hbox{on }C\cup\{x,a\},
        \qquad
        \theta^+(a,y)\quad\hbox{on }C\cup\{a,y\}
\tag{3.3}
\]

are restrictions of one cyclic order on \(C\cup\{x,a,y\}\).  The same
is true with both plus signs replaced by minus signs.

#### Proof

Restrict both orders in (3.3) to \(C\cup\{a\}\).  In the first, \(a\)
occupies the \(B\)-gap of the cyclic order on \(C\); in the second it
occupies the \(A\)-gap.  These are distinct cyclic orders because the
two gaps are distinct.  Restrictions of one ambient cyclic order to the
same subset must agree, a contradiction.  Under the two minus
specializations the roles of \(A,B\) reverse in both edges, giving the
same contradiction. \(\square\)

### Corollary 3.2 (the master-order state is conveyor-free)

The state \(\mathcal S_\sigma\) contains no shore of a distinct-top
common-endpoint two-base conveyor if either endpoint path has at least
two edges.  In particular it contains no shore of the three-top
conveyor and no shore of the symmetric six-frame realization.

It also contains no shore of the six-frame mixed-spectator cycle from
`MATH_THEOREM_SIX_FRAME_MIXED_PLACEHOLDER_RECTANGLE_AND_MINIMALITY_20260726.md`.

#### Proof

Every selected full cyclic frame is \(\sigma|_U\).  Along a path of at
least two edges, two consecutive edge tops share the internal path label
\(a\).  The packet places \(a\) in the \(B\)-gap on one edge and the
\(A\)-gap on the next, or conversely on the other shore.  Lemma 3.1
contradicts the consistency of the two restrictions of \(\sigma\).

The three-top packet has a two-edge path, while each path in the
six-frame realization has three edges.  The mixed-spectator packet has
successive edges in its five-edge common-spectator path, so the same
argument applies. \(\square\)

The conclusion concerns labelled path options, exactly as they occur as
terms of the common-core product polynomial.  It does not quotient away
the full order and core data of two different labelled representations
of the same path monomial.

## 4. The isolated state has large collision energy

Let \(\mathcal A_\sigma\) consist of the middle sets \(D\) whose
complement contains at least one block of \(H\) consecutive coordinates
of the master cyclic order \(\sigma\).

### Lemma 4.1 (support compression)

Every owner used by \(\mathcal S_\sigma\) lies in
\(\mathcal A_\sigma\), and

\[
             |\mathcal A_\sigma|
             \le 2m\binom{2m-H}{m}
             \le 2m\,2^{-H}W.
\tag{4.1}
\]

#### Proof

Suppose the path at \(U\) uses the owner \(D=U\setminus J\), where
\(J\) is one of its omitted \(H\)-windows.  The members of \(J\) are
consecutive in \(\sigma|_U\).  Hence the corresponding arc of
\(\sigma\), from the first member of \(J\) to the last, contains no
member of \(U\setminus J=D\).  The whole arc lies in \(D^c\) and has
at least \(H\) coordinates.  Thus \(D\in\mathcal A_\sigma\).

There are \(2m\) cyclic blocks of length \(H\).  For a fixed block,
the number of middle sets avoiding it is \(\binom{2m-H}{m}\).  The
union bound gives the first inequality in (4.1).  Finally,

\[
 {\binom{2m-H}{m}\over\binom{2m}{m}}
 =\prod_{j=0}^{H-1}{m-j\over2m-j}
 \le2^{-H},
\tag{4.2}
\]

which proves the second. \(\square\)

### Theorem 4.2 (isolated high-energy local minimum)

The state \(\mathcal S_\sigma\) satisfies (0.6).  It is an isolated
vertex, and hence a local minimum, in the labelled state graph generated
by the three-top/two-base conveyor, its symmetric six-frame realization,
and the six-frame mixed-spectator cycle.

#### Proof

The total middle occurrence mass is

\[
                         \sum_DK_D=LN=T=\rho W.
\tag{4.3}
\]

By Lemma 4.1 all nonzero loads lie on a set of size at most
\(2m2^{-H}W\).  Cauchy--Schwarz gives

\[
             \sum_DK_D^2
             \ge {T^2\over|\mathcal A_\sigma|}
             \ge {\rho^2 2^H\over2m}W.
\tag{4.4}
\]

Therefore

\[
\begin{aligned}
 \Psi(\mathcal S_\sigma)
 &=\frac12\left(\sum_DK_D^2-T\right)\\
 &\ge\left({\rho^2 2^H\over4m}-{\rho\over2}\right)W,
\end{aligned}
\tag{4.5}
\]

which is (0.6).  Corollary 3.2 says that no generating exchange has a
shore at this state, so it has no neighbor in the stated move graph.
\(\square\)

For the calibrated \(H\), one has \(2^H/m\to\infty\), so (4.5) is in
particular \(\Omega(W)\).  This construction is deterministic; no
product measure or entropy estimate enters its proof.

## 5. Exact boundary

Proved:

1. the exact \(\Psi\)-derivative (0.3) for every coordinate-conjugate
   common restriction of the two-base conveyor;
2. exact \(\Psi\)-flatness for its complete and protected/inert-hole
   middle-preserving versions;
3. an explicit labelled common-core state containing no three-top,
   six-frame two-base, or mixed-spectator conveyor shore; and
4. the deterministic lower bound (0.6) on that state's collision
   energy.

Not proved:

1. that every high-energy state contains a descending non-inert
   conveyor;
2. that the master-order state remains trapped after arbitrary
   zero-energy changes between different labelled representations of
   one path monomial;
3. a lower bound on \(\min\Psi\); or
4. coefficient one.

The smallest replacement lemma needed by this lane is therefore a
**quotient escape theorem**: after allowing zero-energy changes of
labelled representation, every state with \(\Psi\ge\varepsilon W\)
must reach a state exposing a non-inert conveyor with negative external
score in (0.3).  The present local identities do not imply that lemma.
