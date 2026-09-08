# The support-minimal two-base promotion conveyor uses three tops

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,
\tag{0.1}
\]

and assume \(H\ge2\) and \(M\ge8H\).  There is an explicit exchange of
three actual cyclic frames on three distinct rank-\(M\) tops such that:

1. both shores use exactly one frame on each of the same three tops;
2. both shores are squarefree at the middle row;
3. their complete middle supports are identical;
4. at every \(1\le q\le H\), the direct rank-\((m-q)\) derivative,
   equivalently the root-form rank-\((m+q)\) derivative, has exactly
   \(8q\) coefficients of each sign and squared norm \(16q\);
5. the opposite root-form rank-\((m-q)\) and direct rank-\((m+q)\)
   derivatives are zero;
6. the two shores are coordinate-conjugate, so every floor-corrected
   energy derivative has no quadratic self-toll; and
7. for every prescribed positive depth, one fresh-label fourth frame is
   middle-disjoint from both shores and gives strict floor descent by one
   unit at that depth.

The three changed tops are

\[
 C\cup\{x,y\},\qquad C\cup\{x,a\},\qquad C\cup\{a,y\},
\tag{0.2}
\]

where \(|C|=M-2\) and \(x,a,y\notin C\) are distinct.  Thus the
primitive is strictly smaller than the proposed six- and eight-top
searches.

Three tops are support-minimal among arbitrary squarefree exact-middle
exchanges of complete frames.  The one-top case is rigid by reconstruction of
one cyclic window deck.  In the two-top case, targets containing a
coordinate exclusive to one top fix all windows except one consecutive
block; the retained path reconstructs that block as well.  The full proof
is in Propositions 6.2--6.4.

This is a genuine non-load-neutral legal compound exchange and an exact
finite descent witness.  It is not a charged-coverage theorem: no claim
is made that a positive fraction of an arbitrary global resolution
contains a favorably charged copy.

## 1. The two positional bases

Partition a common core \(C\), \(|C|=M-2\), into eight disjoint ordered
arms and two filler blocks.  The inner arms

\[
 A^-,A^+,B^-,B^+
\tag{1.1}
\]

have length \(H-1\), the outer arms

\[
 \widehat A^-,\widehat A^+,
 \widehat B^-,\widehat B^+
\tag{1.2}
\]

have length \(H\), and \(F_1,F_2\) partition the remaining
\(M-8H+2\) labels.  Arms are listed nearest-to-farthest from their
named placeholder.  Let \(\overleftarrow D\) denote reversal of an
ordered block.

Define two cyclic positional words on \(C\cup\{A,B\}\):

\[
\begin{aligned}
 \omega={}&(
 A,A^+,\widehat A^+,F_1,
 \overleftarrow{\widehat B^-},\overleftarrow{B^-},
 B,B^+,\widehat B^+,F_2,
 \overleftarrow{\widehat A^-},\overleftarrow{A^-}),\\
 \omega'={}&(
 A,B^+,\widehat A^+,F_1,
 \overleftarrow{\widehat B^-},\overleftarrow{A^-},
 B,A^+,\widehat B^+,F_2,
 \overleftarrow{\widehat A^-},\overleftarrow{B^-}).
\end{aligned}
\tag{1.3}
\]

The placeholders have cyclic distance at least \(4H-2\) in both words.
For \(\theta\in\{\omega,\omega'\}\) and distinct labels \(u,v\notin C\),
write \(\theta^+(u,v)\) for the specialization \(A=u,B=v\), and
\(\theta^-(u,v)\) for \(A=v,B=u\).  Let

\[
 d_h(\theta;u,v)
 =c_{\theta^-(u,v)}^h-c_{\theta^+(u,v)}^h
\tag{1.4}
\]

be the derivative of the complete direct \(h\)-interval deck.

For a placeholder \(Z\), let \(K_{Z,t}^{\theta}(h)\) be the
\((h-1)\)-set consisting of the nearest \(t\) predecessor labels and
the nearest \(h-1-t\) successor labels around \(Z\).  Since no
\(h\)-interval with \(h\le2H\) contains both placeholders,

\[
\begin{aligned}
 d_h(\theta;u,v)
 ={}&\sum_{t=0}^{h-1}
   \left(e_{K_{A,t}^{\theta}(h)\cup\{v\}}
        -e_{K_{A,t}^{\theta}(h)\cup\{u\}}\right)\\
 &-\sum_{t=0}^{h-1}
   \left(e_{K_{B,t}^{\theta}(h)\cup\{v\}}
        -e_{K_{B,t}^{\theta}(h)\cup\{u\}}\right).
\end{aligned}
\tag{1.5}
\]

At every \(h\le H\), only inner arms occur.  The inner neighborhoods
are interchanged between the two bases, whence

\[
 \boxed{d_h(\omega';u,v)=-d_h(\omega;u,v)
        \qquad(1\le h\le H).}
\tag{1.6}
\]

At \(h=H+q\), \(1\le q\le H\), the cancellation persists for the
indices

\[
                         q\le t\le H-1,
\tag{1.7}
\]

because those contexts still use inner arms only.  It fails on the
boundary indices

\[
 I_q=\{0,1,\ldots,q-1\}
       \cup\{H,H+1,\ldots,H+q-1\},
\tag{1.8}
\]

where the two occurrences of a fixed inner type meet different outer
arms.  The four context families and the \(2q\) indices in (1.8) give
\(8q\) pairwise distinct core contexts.  Indeed, the number of chosen
predecessor-arm labels recovers \(t\); different inner types use disjoint
inner arms; and the two copies of one inner type use disjoint outer
collars at every boundary index.

Consequently, with

\[
                         g(K)=e_{K\cup\{y\}}-e_{K\cup\{x\}},
\tag{1.9}
\]

the vector

\[
 d_{H+q}(\omega;x,y)+d_{H+q}(\omega';x,y)
\tag{1.10}
\]

has \(8q\) positive and \(8q\) negative coordinates, all distinct.
Thus its squared norm is \(16q\).

## 2. The three-top exchange

Choose distinct \(x,a,y\notin C\) and set

\[
 U_0=C\cup\{x,y\},\qquad
 U_1=C\cup\{x,a\},\qquad
 U_2=C\cup\{a,y\}.
\tag{2.1}
\]

The old shore consists of

\[
 \omega^+(x,y),\qquad
 (\omega')^+(x,a),\qquad
 (\omega')^+(a,y),
\tag{2.2}
\]

on \(U_0,U_1,U_2\), respectively.  The new shore replaces every plus
frame by the corresponding minus frame.

### Theorem 2.1 (exact endpoint telescope)

At every interval length \(h\), the aggregate new-minus-old direct-deck
derivative is

\[
 \boxed{
 \Delta_h=d_h(\omega;x,y)+d_h(\omega';x,y).}
\tag{2.3}
\]

#### Proof

The first summand is the derivative on the direct edge \(xy\).  On the
path \(x,a,y\), every fixed positional interval containing exactly one
of \(A,B\) gives

\[
 (e_{K\cup\{a\}}-e_{K\cup\{x\}})
 +(e_{K\cup\{y\}}-e_{K\cup\{a\}})
 =e_{K\cup\{y\}}-e_{K\cup\{x\}}.
\tag{2.4}
\]

Intervals containing zero or two placeholders have zero derivative.
Thus the path telescopes phase by phase to \(d_h(\omega';x,y)\), proving
(2.3). \(\square\)

Equations (1.6) and (2.3) give

\[
                         \Delta_h=0\qquad(1\le h\le H),
\tag{2.5}
\]

while (1.10) gives

\[
 \boxed{
 \|\Delta_{H+q}\|_0=\|\Delta_{H+q}\|_2^2=16q
 \qquad(1\le q\le H).}
\tag{2.6}
\]

All identities are phasewise before the final deck summation.  Therefore
they survive any common phase deletion whose own derivative is zero in
both bases, and any common phase-to-depth schedule supported on the
displayed contexts.

## 3. Exact middle ownership and the two signed sides

For later complementation, note the following common-core identity.  If
\(K\subseteq C\), \(U_{uv}=C\cup\{u,v\}\), and

\[
 g_K(u,v)=e_{K\cup\{v\}}-e_{K\cup\{u\}},
\]

then complementation inside the actual top \(U_{uv}\) sends

\[
 g_K(u,v)\longmapsto-g_{C\setminus K}(u,v).
\tag{3.0a}
\]

Consequently it commutes with the endpoint telescope:

\[
 \mathcal C_{xa}g_K(x,a)+\mathcal C_{ay}g_K(a,y)
 =\mathcal C_{xy}g_K(x,y).
\tag{3.0b}
\]

This is the reason complementary derivatives telescope even though the
two path edges live on different tops.

Complementation inside the virtual endpoint top

\[
                         U_*=C\cup\{x,y\}=U_0
\tag{3.1}
\]

sends an \(h\)-interval derivative to the derivative of the direct
\((M-h)\)-deck.  Thus \(\Delta_H=0\) implies equality of the aggregate
direct \(m\)-window decks.  Global complementation converts these
windows to the physical root-form middle targets.  Hence the two shores
have identical middle incidence vectors.

### Lemma 3.1 (both middle shores are squarefree)

Every shore contains \(3M\) distinct middle targets.

#### Proof

Work with direct \(m\)-windows and complement each inside its own top.
The complementary \(H\)-window contains at most one placeholder.  If it
contains neither, the \(m\)-window contains both outside labels, whose
unordered pair identifies one of the three distinct edges in (2.1).

If it contains one placeholder, the \(m\)-window contains one outside
label.  A collision can occur only between two edges sharing that label.
At the shared label \(x\), the old shore compares a \(B\)-context in
\(\omega\) with a \(B\)-context in \(\omega'\).  By inner-neighborhood
interchange, the latter is an \(A\)-context in \(\omega\), and the
\(A,B\) context families are disjoint.  At \(y\), the same argument
compares \(A\)-contexts.  At the internal label \(a\), its two path
occurrences occupy opposite placeholder roles, so equality would compare
the disjoint \(A,B\) context families of \(\omega'\).

On the new shore every placeholder role reverses.  The same three
comparisons are merely interchanged, and remain disjoint.  Thus neither
shore has a repeated middle target. \(\square\)

Since the two incidence vectors are equal and squarefree, their supports
are the same set of \(3M\) middle targets.  This is literal preservation
of exact middle ownership.

For \(1\le q\le H\), applying (3.0a)--(3.0b) to (2.6) gives the direct
rank-\((m-q)\) derivative, and global complementation gives the root-form
rank-\((m+q)\) derivative.  Both have squared norm \(16q\).  For
\(1\le q<H\), equation (2.5) at \(h=H-q\) shows that the opposite
root-form rank-\((m-q)\) and direct rank-\((m+q)\) derivatives vanish.
At \(q=H\) the latter assertion is separate: the direct rank-\(M\) deck
consists of the unchanged top, once on each shore.  This is the exact
two-sided all-depth action.

## 4. Exact floor derivative

Let \(\Gamma^0,\Gamma^1\) be the old and new three-frame load vectors in
any one controlled target layer, and let \(R\) be the fixed external
load.  For an integer baseline \(c\), put

\[
 \Phi_c(L)=\frac12\sum_T(L_T-c)(L_T-c-1).
\tag{4.1}
\]

For every zero-sum derivative \(\Delta\), direct expansion gives

\[
 \Phi_c(L+\Delta)-\Phi_c(L)
 =\langle L,\Delta\rangle+\frac12\|\Delta\|_2^2.
\tag{4.2}
\]

The coordinate involution

\[
                         x\leftrightarrow y,qquad a\mapsto a,
 \qquad C\text{ fixed}
\tag{4.3}
\]

fixes \(U_0\), interchanges \(U_1,U_2\), and maps every old plus frame
to the corresponding new minus frame on the reversed edge.  Hence

\[
                         \|\Gamma^0\|_2=\|\Gamma^1\|_2.
\tag{4.4}
\]

Putting \(\Delta=\Gamma^1-\Gamma^0\) in (4.2) therefore yields

\[
 \boxed{
 \Phi_c(R+\Gamma^1)-\Phi_c(R+\Gamma^0)
 =\langle R,\Delta\rangle.}
\tag{4.5}
\]

Thus the move has no self-restitution and no floor-baseline error.

## 5. A middle-squarefree physical descent witness

Fix \(1\le q\le H\) and select one negative target \(T_-\) of the
direct rank-\((m-q)\) derivative.  All derivative targets lie in
\(U_*=C\cup\{x,y\}\).

Choose disjoint fresh sets \(Z,Y\), also disjoint from
\(C\cup\{x,a,y\}\), with

\[
                         |Z|=H+1,\qquad |Y|=q-1.
\tag{5.1}
\]

This is possible whenever \(m-H-1\ge H+q\), in particular under
\(m\ge3H+1\).  Put

\[
                         U_e=T_-\,\dot\cup Z\,\dot\cup Y.
\tag{5.2}
\]

It has size \(M\).  Make \(T_-\) one consecutive block in a cyclic
order \(\pi_e\) of \(U_e\), place a \(Z\)-label at each end of this
block, and separate all remaining \(Y\)-labels from one another by
\(Z\)-labels.  The unique length-\((m-q)\) interval containing no
\(Z\)-label is then \(T_-\).  Since every derivative target avoids
\(Z\),

\[
                         \langle c_{\pi_e}^{m-q},\Delta_q\rangle=-1.
\tag{5.3}
\]

Every middle \(m\)-window of \(\pi_e\) contains a \(Z\)-label: its
complementary \(H\)-window cannot contain all \(H+1\) labels of \(Z\).
No middle target of the three-frame packet contains a \(Z\)-label.
Therefore adjoining \(\pi_e\) preserves middle squarefreeness on both
shores.  Equation (4.5) gives exact floor descent \(-1\) at the
prescribed depth (or \(-2\) for the doubled convention).

This exterior witnesses genuine physical descent while preserving exact
middle ownership.  It does not control its scores at the other positive
depths and does not prove a simultaneous weighted all-depth descent.

## 6. Support minimality inside the path model

A common-endpoint two-base conveyor consists of one path from \(x\) to
\(y\) evaluated in \(\omega\) and one path from \(x\) to \(y\)
evaluated in \(\omega'\), with every path edge realized on its top
\(C\cup\{u,v\}\).  Phasewise telescoping gives (2.3), independently of
the internal vertices.

### Proposition 6.1 (three is minimal in this model)

If all touched tops are distinct, a nontrivial common-endpoint two-base
conveyor uses at least three tops.  The construction above attains three.

#### Proof

Each of the two endpoint paths contains at least one edge.  If their
total number of edges were two, both paths would be the one-edge path
from \(x\) to \(y\).  Both edges would then use the same top
\(C\cup\{x,y\}\), contrary to distinctness of touched tops.  Hence at
least three edges, and therefore three tops, are necessary.  Equations
(2.1)--(2.2) attain the bound. \(\square\)

This proves minimality inside the path model.  We next strengthen it to
absolute minimality among all squarefree full-frame exchanges.

### Proposition 6.2 (absolute one-top no-go)

Let \(2\le H<M/2\). If two full cyclic frames on one fixed top have the
same middle deck, then their cyclic orders differ only by rotation or
reversal. Consequently all their unphased interval decks agree, and a
one-top exact-middle exchange is load-neutral at every depth.

#### Proof

Complement the common middle deck inside the top. This gives the same
family \(\mathcal D\) of cyclic \(H\)-windows for both frames. Join two
members of \(\mathcal D\) when their intersection has size \(H-1\).
Because \(M>2H\), this occurs exactly for consecutive cyclic windows;
the resulting graph is the cycle \(C_M\).

Thus the cyclic sequence of window sets is determined up to rotation and
reversal. After choosing an orientation, the singleton differences
\(S_{i+1}\setminus S_i\) recover the entering labels in cyclic order.
The underlying frame is therefore determined up to the same dihedral
ambiguity, and that ambiguity preserves every unphased interval deck.
\(\square\)

The two-top case follows from a slightly stronger reconstruction lemma.

### Lemma 6.3 (a deck is fixed by the windows missing part of a marked set)

Let \(\pi,\pi'\) be cyclic orders on the same \(M\)-set \(U\), where
\(2\le H<M/2\), and let \(\varnothing\ne E\subseteq U\).  Suppose the
two cyclic \(H\)-window families agree on all windows which do **not**
contain every element of \(E\).  Then the full \(H\)-window families
agree, and \(\pi,\pi'\) differ only by rotation or reversal.

#### Proof

Put \(r=|E|\). If \(r>H\), no \(H\)-window can contain \(E\), so the
hypothesis already gives the full deck and Proposition 6.2 applies. The
same conclusion holds for any \(r\) if no containing window exists.
Otherwise, in either
cyclic order, the start positions of the \(H\)-windows containing all of
\(E\) form one consecutive interval.  Indeed, cut the cycle immediately
before the first element of the unique length-at-most-\(H\) arc spanning
\(E\).  If that arc has \(s\) positions, its containing-window starts
form an interval of length

\[
                         t=H-s+1\le H-r+1.          \tag{6.1}
\]

The two retained families are equal, so their cardinalities, and hence
their omitted-block lengths \(t\), are equal. Thus the retained windows
form one common consecutive path of length
\(L=M-t\).  Their abstract order is determined, up to reversal, by
joining two retained sets when their intersection has size \(H-1\): as
in Proposition 6.2, these are exactly consecutive cyclic windows.  Since
\(L\ge M-H>H\), this path contains enough windows for reconstruction.

Write the ordered retained path as \(S_0,S_1,\ldots,S_{L-1}\).  The
successive leaving labels

\[
                         S_i\setminus S_{i+1}
                         \qquad(0\le i\le H-1)
\]

order all \(H\) labels of \(S_0\), and the entering labels
\(S_{i+1}\setminus S_i\), \(0\le i\le L-2\), extend this to a linear
word segment of length

\[
                         H+L-1=H+M-t-1.             \tag{6.2}
\]

If \(r\ge2\), (6.1) makes (6.2) at least \(M+r-2\ge M\), so it
recovers the entire cyclic order.  If \(r=1\), then exactly \(H\)
windows contain the marked element, so \(t=H\).  The reconstructed
segment has length \(M-1\) and consists of all unmarked labels; the known
marked label occupies the unique gap between its two ends.  Again the
whole cyclic order is determined.  The only choice throughout was
reversal (and the irrelevant cyclic starting point).  \(\square\)

### Proposition 6.4 (absolute two-top no-go for complete frames)

Let two squarefree old frames on distinct tops \(U,V\) and two
squarefree new frames on the same respective tops have identical
aggregate middle support.  Then each new frame is dihedrally equivalent
to the old frame on its own top.  Consequently every two-top
exact-middle exchange is load-neutral at every depth.

#### Proof

Apply global complementation to the common physical middle support, so
that it becomes the common union of two squarefree direct \(m\)-window
decks.  Put \(E=U\setminus V\), which is nonempty because the tops are
distinct and have equal size.

Every old \(U\)-window \(X\) with \(X\cap E\ne\varnothing\) cannot be a
window on \(V\).  Equality and squarefreeness of the two unions therefore
force \(X\) to belong to the new \(U\)-deck.  The converse follows after
interchanging old and new.  Hence the old and new \(U\)-decks agree on
all direct \(m\)-windows meeting \(E\).

Complement inside \(U\).  A direct window \(X\) meets \(E\) exactly
when its complementary \(H\)-window does not contain all of \(E\).
Lemma 6.3 now makes the two frames on \(U\) dihedrally equivalent.
Repeating the argument with \(V\setminus U\) fixes the frame on \(V\).
Dihedral changes preserve every unphased interval deck, proving the
claim. \(\square\)

Hence the absolute minimum support for complete frames is exactly

\[
                         \boxed{d_{\min}^{\rm full}=3}. \tag{6.3}
\]

This lower bound also applies to a marked protected deletion when the
same deleted target on each top is specified on both shores: restore
those targets and invoke Proposition 6.4.  It does **not** apply verbatim
to arbitrary punctured frames with moving, unmarked deleted phases, since
their common punctured support need not determine which full-deck targets
must be restored.  The construction itself does admit the protected
deletion described after (2.6), but absolute minimality in the unrestricted
punctured category remains open.

## 7. Exact boundary

Proved:

1. a three-top compound exchange of literal cyclic frames;
2. squarefree and identical middle support on both shores;
3. exact one-sided positive-depth action \(16q\) and zero action on the
   opposite sign;
4. exact floor-baseline cancellation;
5. an exact-middle-compatible physical descent at every prescribed
   depth;
6. support minimality in the common-endpoint two-base path model; and
7. absolute one- and two-top rigidity for complete frames, proving that
   three tops are globally minimal in that category.

The exact moved support over the nonzero signed side is

\[
 \sum_{q=1}^H\|\Delta_q\|_0
 =16\sum_{q=1}^Hq
 =8H(H+1).
\tag{7.1}
\]

At the calibrated scale \(H=O(\sqrt{m\log m})\), this is
\(O(m\log m)=o(W)\), where \(W=\binom{2m}{m}\).  The packet changes
three frame variables and the favorable witness adds one fixed frame;
there is no hidden factor depending on \(M\) in (7.1).

Not proved:

1. a favorable charge simultaneously at all depths;
2. a dense owner-disjoint packing of these three-top packets;
3. an iterative contraction or aggregate \(o(W)\) floor theorem; or
4. coefficient one.

The surviving global gate is a charged coverage theorem for the
\(8q\) boundary contexts on each sign, subject to overlap among their
three touched tops.
