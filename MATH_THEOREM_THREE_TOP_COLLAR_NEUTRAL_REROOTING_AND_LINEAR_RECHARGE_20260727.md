# A three-top collar-neutral tail change joins distinct boundary-swap components

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad \kappa=4H-1,\qquad
 d=M-\kappa=m-3H+1,
\tag{0.1}
\]

and assume \(H\ge3\), \(M\ge 8H+1\).  There is an explicit exchange
on three rank-\(M\) tops with the following properties.

1. Each shore has one literal rooted length-\(d\) tight path on each
   of the same three tops.
2. At every interval length \(0\le h\le2H\), the aggregate physical
   target derivative is exactly zero.
3. Both middle shores are squarefree and have exactly the same set of
   \(3d\) middle owners.
4. On a designated focal top the old and new rooted words begin

   \[
       (r_1,r_2,x,\ldots,y,\ldots),\qquad
       (r_1,r_2,y,\ldots,x,\ldots).
   \tag{0.2}
   \]

   Hence they lie in different first-two-swap \(K_2\)-components.
   More strongly, the first-two boundary swap has different literal
   length-\(2\) and different middle traces on the two states.
5. In the safe-restorable category used below, support three is
   minimal: one- and two-top exchanges with the same ordered two-letter
   port cannot change a boundary-swap component.
6. The construction is reusable locally.  On one focal top it can
   bring \(m-O(H)\) different labels successively into position three,
   using two fresh companion tops per step.  Each step is an exact
   coefficient-one packet and preserves the entire protected trace
   ledger.  Thus the local recharge throughput is \(\Theta(m)\), not
   \(O(1)\).

The construction is the smallest literal escape from the fixed
\(K_2\)-per-top obstruction in the natural fixed-port, restorable-hole
model.  It is not yet a global coefficient-one factor theorem: a
pre-existing table must contain the two companion source paths at each
step.  If it does, replacement preserves its middle incidence vector
exactly and hence cannot create a new owner repeat.  The remaining
gate is simultaneous source-packet installation, not a local collar or
chronology obstruction.

There is an important semantic distinction.  A useful re-rooting cannot
fix the focal ordered \(H\)-prefix pointwise, because that prefix
determines the boundary-swap trace through length \(H\).  The theorem
preserves the **aggregate** collar exactly; the focal third letter is
changed and the two companion rows cancel that change at every protected
length.

## 1. Rooted retained decks

Let \(U\) be an \(M\)-set and let \(\pi\) be a cyclic order on \(U\).
For a set \(S\) of phase starts and \(0\le h\le2H\), write the omitted-
interval and physical complement-target decks as

\[
 {\cal C}_h(\pi;S)=\sum_{s\in S}e_{I_h(\pi,s)},
 \qquad
 {\cal D}_h(U,\pi;S)
 =\sum_{s\in S}e_{\,U\setminus I_h(\pi,s)},
\tag{1.1}
\]

where \(I_h(\pi,s)\) is the forward cyclic interval of length \(h\)
starting at \(s\), and \(I_0=\varnothing\).  If the omitted phase starts
form one cyclic interval of length \(\kappa\), then the retained starts
form one interval of length \(d=M-\kappa\).  Starting at its first phase
and reading far enough for intervals of length at most \(2H\) gives one
literal injective word of length

\[
                         d+2H-1=M-2H<M.
\tag{1.2}
\]

Thus (1.1) is a literal linear tight-path deck, not a formal cyclic
average.

For a positional cyclic order \(\theta\) on
\(C\cup\{A,B\}\), and distinct \(u,v\notin C\), let
\(\theta^+(u,v)\) put \(A=u,B=v\), and let \(\theta^-(u,v)\)
put \(A=v,B=u\).  Define the retained derivatives

\[
 c_h^S(\theta;u,v)
 ={\cal C}_h(\theta^-(u,v);S)
  -{\cal C}_h(\theta^+(u,v);S),
\tag{1.3a}
\]

and

\[
 d_h^S(\theta;u,v)
 ={\cal D}_h(C\cup\{u,v\},\theta^-(u,v);S)
  -{\cal D}_h(C\cup\{u,v\},\theta^+(u,v);S).
\tag{1.3b}
\]

Only intervals containing exactly one placeholder contribute.

## 2. Two bases with opposite complete \(2H\)-collars

Put

\[
                         L=2H-1.
\tag{2.1}
\]

Partition the common core \(C\), \(|C|=M-2\), into four disjoint
ordered arms

\[
 A^+,A^-,B^+,B^-,\qquad |A^\pm|=|B^\pm|=L,
\tag{2.2}
\]

and two filler words \(F_1,F_2\).  We require \(|F_2|\ge3\); this is
possible under \(M\ge8H+1\).  Define

\[
\begin{aligned}
 \omega={}&(A,A^+,F_1,\overleftarrow{B^-},
              B,B^+,F_2,\overleftarrow{A^-}),\\
 \eta={}&(A,B^+,F_2,\overleftarrow{A^-},
              B,A^+,F_1,\overleftarrow{B^-}).
\end{aligned}
\tag{2.3}
\]

The radius-\(L\) predecessor/successor context of \(A\) in \(\eta\)
is the context of \(B\) in \(\omega\), and the context of \(B\) in
\(\eta\) is the context of \(A\) in \(\omega\).  Since an interval of
length at most \(2H\) uses at most \(2H-1=L\) context letters, this
identity is exact throughout the protected collar.

For a core context \(K\), put

\[
                 g_K(u,v)=e_{K\cup\{v\}}-e_{K\cup\{u\}}.
\tag{2.4}
\]

In the omitted-interval ledger, the complete cyclic derivative at a
placeholder is the sum of the
appropriate \(g_K\)'s; the \(A\)-sum has positive sign and the
\(B\)-sum negative sign.  Interchanging the two context palettes
therefore gives the exact identity

\[
             \boxed{c_h^{\rm cyc}(\eta;u,v)
                    =-c_h^{\rm cyc}(\omega;u,v)}
             \qquad(0\le h\le2H).
\tag{2.5}
\]

Complementation inside the common top \(C\cup\{u,v\}\) is a linear
coordinate bijection.  Hence the physical derivatives obey the same
anti-collar identity

\[
             \boxed{d_h^{\rm cyc}(\eta;u,v)
                    =-d_h^{\rm cyc}(\omega;u,v)}.
\tag{2.6}
\]

The cases \(h=0,1\) are also immediate: at \(h=0\) nothing changes,
and at \(h=1\) the two singleton phases are merely exchanged.

This is the only modification needed relative to the two-base
promotion conveyor: arms of length \(H-1\) give cancellation only up
to \(H\), whereas arms of length \(2H-1\) give cancellation throughout
the entire \(2H\)-collar.

## 3. Matched phase cuts with the placeholder in position three

The directed arc from \(B\) to \(A\) in \(\omega\), after deleting
its endpoint placeholders, is

\[
                  B^+,F_2,\overleftarrow{A^-}.
\tag{3.1}
\]

The directed arc from \(A\) to \(B\) in \(\eta\) has the identical
labelled word (3.1).  Its length is at least

\[
                    2L+3=4H+1=\kappa+2.
\tag{3.2}
\]

Choose a block \(D_\omega\) of \(\kappa\) consecutive phase starts on
(3.1) so that exactly two starts remain between the end of the block
and \(A\).  Choose the identically labelled block \(D_\eta\) on the
copy of (3.1) which precedes \(B\) in \(\eta\).  Put

\[
             S_\omega=U\setminus D_\omega,
             \qquad S_\eta=U\setminus D_\eta,
\tag{3.3}
\]

where the notation means the complementary sets of phase starts.
Both retained paths have \(d\) phases.  The \(\omega\)-path starts two
letters before \(A\), and the \(\eta\)-path starts two letters before
\(B\).

### Lemma 3.1 (the deleted ledgers are opposite)

For every \(0\le h\le2H\), both the omitted-interval and physical
deleted ledgers are opposite:

\[
 c_h^{D_\eta}(\eta;u,v)
 =-c_h^{D_\omega}(\omega;u,v),
 \qquad
 d_h^{D_\eta}(\eta;u,v)
 =-d_h^{D_\omega}(\omega;u,v).
\tag{3.4}
\]

#### Proof

An interval starting in \(D_\omega\) which misses \(A\) contains no
placeholder at all: the block lies strictly after \(B\) on the directed
\(B\)-to-\(A\) arc, so a forward interval cannot return to \(B\), and
it cannot reach the next placeholder \(A\) by hypothesis.  Its
plus/minus derivative is zero.  If it reaches \(A\), the identically
labelled start in \(D_\eta\) reaches \(B\), with exactly the same core
context.  The two placeholder contributions have opposite signs.
This pairs every nonzero omitted-interval term.  Complementation in the
fixed top gives the physical identity.  The argument with
\(\omega,\eta\) interchanged is identical, proving (3.4). \(\square\)

Subtracting (3.4) from (2.5)--(2.6) gives the retained identities

\[
             c_h^{S_\eta}(\eta;u,v)
                    =-c_h^{S_\omega}(\omega;u,v),
 \qquad
             \boxed{d_h^{S_\eta}(\eta;u,v)
                    =-d_h^{S_\omega}(\omega;u,v)}
             \qquad(0\le h\le2H).
\tag{3.5}
\]

This is the exact collar ledger after the linear phase cut.

## 4. The three-top telescope

Choose distinct \(x,a,y\notin C\), and put

\[
 U_0=C\cup\{x,y\},\qquad
 U_1=C\cup\{x,a\},\qquad
 U_2=C\cup\{a,y\}.
\tag{4.1}
\]

The old shore is

\[
 (\omega^+(x,y),S_\omega),\qquad
 (\eta^+(x,a),S_\eta),\qquad
 (\eta^+(a,y),S_\eta),
\tag{4.2}
\]

and the new shore replaces all three plus states by their minus states.

### Theorem 4.1 (literal collar-neutral re-rooting)

For every \(0\le h\le2H\), the aggregate new-minus-old physical deck
derivative is zero:

\[
                         \boxed{\Delta_h=0.}
\tag{4.3}
\]

#### Proof

For a fixed positional context, the two path edges telescope:

\[
              g_K(x,a)+g_K(a,y)=g_K(x,y).
\tag{4.4}
\]

Hence the three omitted-interval derivatives in (4.2) sum to

\[
 c_h^{S_\omega}(\omega;x,y)
 +c_h^{S_\eta}(\eta;x,y)=0
\tag{4.5}
\]

by (3.5).

For completeness, the same identity holds for the physical complement
targets in (1.1), even though the three complements are taken in
different tops.  On the top \(C\cup\{u,v\}\), complementation sends

\[
                  g_K(u,v)\longmapsto-g_{C\setminus K}(u,v).
\tag{4.6}
\]

Thus complementation commutes with the endpoint telescope (4.4), with
one common minus sign and the common replacement \(K\mapsto C\setminus
K\).  Equation (4.5) therefore proves (4.3) in the physical target
coordinates. \(\square\)

No asymptotic cancellation appears in (4.3).  Every protected lower and
upper trace, including the middle row \(h=H\), is preserved exactly.

## 5. Exact middle-owner audit

We next verify that equality at \(h=H\) is a coefficient-one identity,
not equality between multisets containing repeats.

### Lemma 5.1 (squarefree shores)

Each shore of (4.2) contains \(3d\) distinct middle owners.

#### Proof

First restore the deleted phases and work with the complete cyclic
frames.  Inside one frame the cyclic \(H\)-windows are distinct because
the word is injective and \(M>2H\).

An \(H\)-window contains at most one placeholder.  If it contains no
placeholder, its complementary middle owner contains both outside
labels; their unordered pair identifies one of the three tops in
(4.1).

Suppose it contains one placeholder.  A collision can then occur only
between two tops sharing the one outside label retained by the owner.
At the shared label \(x\), the old shore compares a \(B\)-context in
\(\omega\) with a \(B\)-context in \(\eta\).  The latter is the
corresponding \(A\)-context in \(\omega\), and the \(A\)- and
\(B\)-context palettes are disjoint because their radius-\((H-1)\)
arms are disjoint.  The same argument applies at \(y\).  At the
internal label \(a\), the two occurrences have opposite placeholder
roles, again comparing disjoint \(A,B\) context palettes.  Reversing
all placeholder roles proves the new-shore assertion.

Thus the two complete shores are squarefree.  Deleting phase starts
cannot create a collision, so both retained shores are squarefree as
well. \(\square\)

Equation (4.3) at \(h=H\) says that the two \(0\)-\(1\) incidence
vectors are equal.  Lemma 5.1 says each has mass \(3d\).  Therefore

\[
 \boxed{
   \operatorname{supp}\operatorname{mid}({\cal O})
   =\operatorname{supp}\operatorname{mid}({\cal N}),
   \qquad |\operatorname{supp}|=3d.}
\tag{5.1}
\]

This is literal exact middle ownership on both shores.

## 6. The focal boundary involution really changes

Let \(r_1,r_2\) be the two labels between \(D_\omega\) and \(A\).
On \(U_0\), the old and new rooted words have the form

\[
\begin{aligned}
 p&=(r_1,r_2,x,c_2,c_3,\ldots,y,\ldots),\\
 q&=(r_1,r_2,y,c_2,c_3,\ldots,x,\ldots).
\end{aligned}
\tag{6.1}
\]

The second placeholder lies beyond the radius-\(2H\) neighborhood of
the first.  In particular it does not occur among
\(c_2,\ldots,c_{H-1}\).

For a rooted word \(w=(u,v,c_1,c_2,\ldots)\), let \(B(w)\) interchange
its first two letters.  Its exact derivative at length \(h\ge2\) is

\[
 {\cal D}_h(B(w))-{\cal D}_h(w)
 =e_{K_h(w)\cup\{v\}}-e_{K_h(w)\cup\{u\}},
\qquad
 K_h(w)=U\setminus\{u,v,c_1,\ldots,c_{h-1}\}.
\tag{6.2}
\]

Applied at \(h=2\), (6.1) gives the two different derivatives

\[
\begin{aligned}
 \partial_2B(p)
   &=e_{K_x\cup\{r_2\}}-e_{K_x\cup\{r_1\}},
   &K_x&=U_0\setminus\{r_1,r_2,x\},\\
 \partial_2B(q)
   &=e_{K_y\cup\{r_2\}}-e_{K_y\cup\{r_1\}},
   &K_y&=U_0\setminus\{r_1,r_2,y\}.
\end{aligned}
\tag{6.3}
\]

They are unequal.  At the middle length the same calculation gives

\[
 K_H(p)=U_0\setminus\{r_1,r_2,x,c_2,\ldots,c_{H-1}\},
\quad
 K_H(q)=U_0\setminus\{r_1,r_2,y,c_2,\ldots,c_{H-1}\},
\tag{6.4}
\]

so the middle unit edges are unequal as well.

Moreover \(q\ne p\) and \(q\ne B(p)\), because the first two letters
agree while the third does not.  Thus the neutral exchange (4.2) joins
two distinct intrinsic \(K_2\)-components and changes the actual
rectangle involution seen by the protected traces.  It is not a
permutation of the invisible final \(2H\) letters.

### Lemma 6.1 (why pointwise collar fixation is impossible)

If two focal rooted words have the same ordered prefix through position
\(H+1\), then their boundary-swap derivatives agree at every
\(2\le h\le H\).

#### Proof

Formula (6.2) depends only on the first \(h+1\) letters. \(\square\)

Consequently a primitive that changes the rectangle involution must
change the focal collar.  Exact collar neutrality can only mean exact
**aggregate** cancellation, which is precisely (4.3).

## 7. Support minimality in the restorable fixed-port category

Call a punctured exchange **safely restorable** if its omitted phase
blocks can be restored on both shores and the restored aggregate middle
derivative is still zero.  Require also that the ordered first two
letters on every touched top agree on the two shores.  These are the
literal data needed to splice the same oriented boundary port before
and after the exchange.  The packet above is safely restorable by
(2.5) and (3.4), and it fixes \((r_1,r_2)\) at the focal top.

### Theorem 7.1 (three is minimal)

No safely restorable one- or two-top squarefree exchange can change a
top's boundary-swap component.  Hence (4.2) has minimum support in this
category.

#### Proof

Restore the omitted phases.  On one fixed top, equality of the middle
deck is equivalent, after complementation, to equality of the cyclic
family of \(H\)-windows.  Joining two windows when their intersection
has size \(H-1\) recovers the cycle \(C_M\), since \(M>2H\).  Successive
set differences then recover the cyclic label order up to rotation and
reversal.  The common ordered first-two port removes both ambiguities,
so the frame is unchanged.

For two distinct tops \(U,V\), put \(E=U\setminus V\ne\varnothing\).
Every direct middle window on \(U\) meeting \(E\) cannot occur on
\(V\).  Squarefreeness and equality of the two-shore union therefore
force all such windows to remain on \(U\).  Complementing in \(U\),
the old and new cyclic \(H\)-window families agree on every window not
containing all of \(E\).

Those common windows form a cyclic path obtained by deleting one
consecutive block of at most \(H-|E|+1\) starts.  Its length is at least
\(M-H>H\).  Consecutive intersections reconstruct this path, and the
leaving/entering singleton differences reconstruct the whole cyclic
order; if \(|E|=1\), the unique missing label occupies the unique
remaining gap.  Thus the two frames on \(U\) are dihedrally equivalent.
The same argument applies to \(V\).  Again the ordered first-two ports
remove the dihedral ambiguity.  Restoring the punctures therefore
leaves the same rooted frames, so no boundary component changes.
\(\square\)

The qualifier “safely restorable” is essential.  The theorem does not
claim a classification of arbitrary shore-dependent moving punctures
whose deleted ledgers do not match.  Such a two-top exception, if it
exists, would require its nontriviality to live entirely in the moving
hole and would not be a fixed-port splice primitive of the present
kind.

## 8. Linear local recharge throughput

The construction is not limited to one prescribed pair of labels.
Fix a focal rooted cyclic order and its phase cut.  Let \(A\) be the
third position of the rooted word.  A position \(B\) is **remote** if
each of the two open cyclic arcs between \(A\) and \(B\) contains at
least \(4H+1\) positions, and if \(B\) is not in the omitted endpoint
block.  There are

\[
                         M-O(H)=m-O(H)
\tag{8.1}
\]

remote positions.

For any remote \(B\), declare the current labels at \(A,B\) to be
\(x,y\), take \(C=U\setminus\{x,y\}\), and use the actual radius-
\((2H-1)\) neighborhoods as the four arms in Section 2.  The remaining
labels are the fillers.  Thus Theorem 4.1 swaps the labels at \(A,B\)
on the focal top while preserving all protected aggregate decks.

Choose a fresh catalyst label

\[
                         a\in[2m]\setminus U.
\tag{8.2}
\]

The two companion tops are

\[
                         U-y+a,\qquad U-x+a.
\tag{8.3}
\]

If different steps use different catalyst labels, all their companion
tops are distinct: the top from a step with catalyst \(a\) contains
\(a\) and contains no other fresh catalyst label.

### Theorem 8.1 (\(m-O(H)\) successive recharges at one top)

There is a literal sequence of

\[
                         t\le m-O(H)
\tag{8.4}
\]

three-top collar-neutral exchanges which:

1. uses one fixed focal top and \(2t\) distinct companion tops;
2. preserves every aggregate deck \({\cal D}_h\),
   \(0\le h\le2H\), after every step;
3. preserves the exact global middle incidence vector after every step;
4. keeps one path per touched top throughout; and
5. exposes \(t+1\) distinct labels successively in focal position three,
   hence \(t+1\) distinct boundary-swap traces by (6.3).

#### Proof

Choose \(t\) distinct remote positions and \(t\) distinct catalyst
labels outside \(U\).  At step \(j\), swap the current position-three
label with the label at the \(j\)-th remote position by the packet of
Theorem 4.1.  The two new companion tops (8.3) have not appeared in an
earlier step.  Leave their switched frames in place; later steps do not
touch them.  Equations (4.3) and (5.1) prove the trace and middle claims
step by step.  Distinct remote labels give distinct position-three
labels, and (6.3) gives distinct boundary-swap traces. \(\square\)

The count (8.4) is the requested reusable local throughput.  It has the
right order to overcome the old one-shot bound of one odd toggle per
top.  It does not by itself choose all source companion paths inside one
global owner resolution.

### Coefficient-one preservation statement

At each step both packet shores are squarefree and have the same middle
support.  Therefore, if the current global table is coefficient one and
contains the three source paths of that step, replacing them by the
three target paths leaves every owner multiplicity unchanged.  In
particular coefficient one is preserved exactly.  What is not proved is
that a prescribed global table contains a simultaneous compatible
choice of the \(2t\) fresh companion source paths.  This is a literal
source-allocation problem, not a multiplicity defect of the primitive.

## 9. Exact implication boundary

Proved:

1. the \(2H-1\)-arm anti-collar identity (2.5);
2. matched length-\(\kappa\) phase cuts putting the focal placeholder in
   position three while preserving the anti-collar identity;
3. a literal three-top exchange with \(\Delta_h=0\) for every
   \(0\le h\le2H\);
4. squarefree, identical middle-owner supports of size \(3d\);
5. a genuine change of the focal boundary-swap trace and of its
   intrinsic \(K_2\)-component;
6. support minimality in the safely restorable fixed-two-port category;
   and
7. a local open schedule with \(m-O(H)\) distinct recharges and fresh
   companion tops.

Not proved:

1. an absolute two-top classification with arbitrary unmatched moving
   punctures;
2. a global coefficient-one packing of all companion source triples;
3. compatibility with a preassigned PBBS/MSW phase-tag history; or
4. a near-\(W\) literal word obtained by splicing a positive-density
   family of the recharge schedules.

The earlier fixed-rectangle parity obstruction is therefore not a
universal bounded-support invariant.  It is broken by a support-three
literal packet.  The surviving coefficient-one question has moved from
local chronology to global source-packet installation.
