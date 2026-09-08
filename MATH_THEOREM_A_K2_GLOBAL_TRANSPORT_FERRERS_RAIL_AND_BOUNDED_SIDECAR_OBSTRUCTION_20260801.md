# The inherited K2 transport bank has a Ferrers OR rail but no O(1)-letter local sidecar

Date: 2026-08-01  
Lane: A, split-pivot global transport / frozen-prefix erosion  
Status: exact plateau and jump address ledgers; exact abstract common-source
OR rail; exact bounded-sidecar obstruction for a fresh pairwise-disjoint
packet.  On inherited shared-bank descendants the address ledger remains
exact but target values may collide and must be quotiented anew.  No
bounded-defect recurrence is claimed.

## 0. Verdict

Let

\[
 W_h=E_h^-A_h^-(j)[X]A_h^+(s)E_h^+
\]

be the repaired depth-\(h\) split-pivot source, with
\(1\le j<h\), \(2\le s\le h\), and positions indexed
\(0,\ldots,4h\).

The remaining transport row does not form a laminar bounded sidecar.

1. On a plateau, six literal source positions acquire the new coordinate
   \(\beta\).  An old untagged occurrence survives at its natural address
   exactly when its interval avoids those six positions.  In particular,
   all \(3h\) native parent lower-q1 occurrences are displaced.
2. On a jump, old packet-internal intervals crossing the two outer block
   seams acquire \(\alpha\) or \(\gamma\).  Their addresses form two
   Ferrers grids.  For a fresh pairwise-disjoint packet these give exactly
   \(5h^2+2h\) distinct values, none occurring inside the child packet.
   After inherited bank sharing, this remains the address count but values
   may collide.
3. Each Ferrers grid has an explicit one-word common-source OR realization;
   a literal parent-shaped copy realizes the whole bank before ambient
   caps and mixed rows are imposed.  Thus bare semantic OR compatibility is
   not the obstruction.
4. In the fresh-bank case every standalone host of the complete bank has
   length \(\Omega(h)\).  Under the separated-marginal architecture, an
   exact frozen-separator cut also forces an unbounded number of exterior
   signatures.  The first nonlaminar example is the \(h=2\) Boolean
   diamond.

Hence a bounded-defect recurrence cannot append an \(O(1)\)-letter local
repair.  It must embed a parent-shaped/Ferrers rail into an already-budgeted
ordinary child sector, or prove a global alternate-occurrence matching.
That matching and the common frozen-prefix replay remain open.

## 1. Frozen overflow

For a fixed source position \(p\), let its literal letter be frozen.  If a
required target \(T\) omits a coordinate \(z\), no exact target interval
for \(T\) may contain a frozen letter containing \(z\).

### Lemma 1.1 (frozen-overflow certificate)

Let \(I\) be a proposed exact row with target \(T\).  If a frozen source
letter \(F_p\), \(p\in I\), contains \(z\notin T\), the relative maximal
erosion equations have no solution.

#### Proof

Every source realizing the frozen prefix has
\(z\in F_p\subseteq\bigcup_{u\in I}Q_u\), whereas exactness requires this
union to equal \(T\). \(\square\)

This is a one-row obstruction.  It cannot be repaired by changing a later
continuation letter.

## 2. Plateau ledger

On a plateau put \(B'=B+\beta\), \(C'=C+\beta\), and keep \((j,s)\).
Exactly the following positions acquire \(\beta\):

\[
\begin{aligned}
 Z_L&=\{h-2,\ h+j-1,\ 2h-1\},\\
 Z_R&=\{2h+1,\ 2h+s,\ 3h+2\},\\
 Z_\beta&=Z_L\mathbin{\dot\cup}Z_R.                  \tag{2.1}
\end{aligned}
\]

### Theorem 2.1 (exact plateau transport)

For every parent interval \(I\subseteq[0,4h]\),

\[
 \operatorname{OR}_{W_h^\beta}(I)
 =\operatorname{OR}_{W_h}(I)\cup
   \begin{cases}
      \{\beta\},&I\cap Z_\beta\ne\varnothing,\\
      \varnothing,&I\cap Z_\beta=\varnothing.
   \end{cases}                                        \tag{2.2}
\]

Thus a naturally transported old untagged row passes frozen-prefix erosion
iff its interval avoids \(Z_\beta\).

#### Proof

The four letters containing \(C\), and precisely the two enriched letters,
are the six positions in (2.1).  Plateau substitution adds \(\beta\) to
each of them and changes no other source letter.  Taking interval unions
gives (2.2), and Lemma 1.1 gives the last assertion. \(\square\)

The complement of \(Z_\beta\) is a union of seven possibly empty linear gaps.  Hence all
local candidate addresses for an untagged target lie wholly in one of
those gaps.

### Corollary 2.2 (the q1 antichain is globally exported)

Every one of the \(3h\) native parent lower-q1 intervals meets
\(Z_\beta\).  Their parent values \(J_1,\ldots,J_{3h}\) are distinct
rank-\((r-1)\) sets, while their native plateau values are
\(J_i+\beta\).  Therefore the old \(J_i\) form a \(3h\)-element antichain
whose natural occurrences all leave the untagged sector.

If \(C\ne\varnothing\), none of the \(J_i\) has any other occurrence in
the local plateau packet.

#### Proof

The starts of the shared length-\(h\) intervals are \(1,\ldots,3h\).
Before the first point of \(Z_\beta\), after the last, and between every
two consecutive points of \(Z_\beta\), there are fewer than \(h\)
untagged positions.  Hence every length-\(h\) interval meets
\(Z_\beta\).  Q1 injectivity gives distinctness and equal rank gives the
antichain.

For \(c\in C\), the only local source letters containing \(c\) are the six
letters in (2.1), all of which contain \(\beta\) after the plateau.  Every
\(J_i\) contains \(C\), so an untagged local interval cannot equal it.
\(\square\)

There is a small exact negative-screen calculation.  Let
\(\mathcal D_\beta\) be all parent interval values whose natural address
meets \(Z_\beta\).  Then

\[
                         \bigcap_{T\in\mathcal D_\beta}T=C. \tag{2.3}
\]

Indeed every tagged letter contains \(C\), and the six one-letter target
values intersect exactly in \(C\).  Thus one nonzero target-side anchor
common to the whole displaced bank exists iff \(C\ne\varnothing\).  If
\(C=\varnothing\), two anchors are necessary and sufficient at the
containment level: \(x_L\) hits every \(Z_L\)-target and \(x_R\) hits every
\(Z_R\)-target.  This is only a negative-cap statement; it neither
reconstructs the rows nor supplies distinct occurrence cells.

## 3. Jump ledger and Ferrers grids

At a deadline jump the inherited literal word is

\[
 J_h=[\gamma]E_h^-[\alpha]A_h^-(j)[X]
          A_h^+(s)[\gamma]E_h^+[\alpha].               \tag{3.1}
\]

Map each old source position to its copy in (3.1), and map an old interval
to the convex hull of its copied endpoints.

### Theorem 3.1 (exact jump transport)

For every parent interval \(I\),

\[
\begin{aligned}
 \operatorname{OR}_{J_h}(\iota I)
  =\operatorname{OR}_{W_h}(I)
   &\cup\bigl(\{\alpha\}:I\text{ crosses }E_h^-|A_h^-(j)\bigr)\\
   &\cup\bigl(\{\gamma\}:I\text{ crosses }A_h^+(s)|E_h^+\bigr).
                                                               \tag{3.2}
\end{aligned}
\]

The two crossing families are exactly the old rows lost at their natural
addresses among intervals whose two endpoints lie in the packet.  Old rows
crossing from the packet into the exterior are additional mixed rows and
are not counted below.

#### Proof

The initial \(\gamma\) and terminal \(\alpha\) lie outside every mapped
old hull.  The internal \(\alpha\) lies in a hull exactly when its endpoints
straddle the left seam, and the internal \(\gamma\) exactly when they
straddle the right seam.  Every other letter in the hull is an old letter.
\(\square\)

For the left seam, number nonempty suffixes of \(E_h^-\) by
\(L_1\supsetneq\cdots\supsetneq L_h\), and prefixes of the following
\(3h+1\) parent letters by
\(P_1\subsetneq\cdots\subsetneq P_{3h+1}\), where the symbols denote their
OR values.  The crossing target deck is

\[
                         T^-_{a,b}=L_a\cup P_b.          \tag{3.3}
\]

This is a Ferrers product.  The right seam is the suffix-prefix dual.

### Theorem 3.2 (fresh-bank size, distinctness, and local absence)

Assume the parent packet banks are pairwise disjoint.  The union of the two
jump casualty grids contains exactly

\[
          2h(3h+1)-h^2=5h^2+2h                         \tag{3.4}
\]

distinct old target values.  None occurs as an interval OR inside the
child packet \(J_h\).

#### Proof

Every left grid value contains the unique coordinates \(q^-\) and
\(\lambda_1\).  Moving either endpoint through its bank changes a fresh
\(d^-\), \(\lambda\), \(x_R\), \(\rho\), \(q^+\), or \(d^+\) endpoint
signature, so all \(h(3h+1)\) left values are distinct.  The right statement
is symmetric.  A value lies in both grids exactly when its old interval
starts in \(E_h^-\) and ends in \(E_h^+\), giving \(h^2\) overlaps.  The
special labels distinguish every other left/right pair, proving (3.4).

Inside \(J_h\), the occurrence of \(q^-\) lies before \(\alpha\), and
every occurrence of the current \(\lambda_1\) lies after it.  Any interval
containing both also contains \(\alpha\), which is absent from an old
target.  Thus no left value occurs.  Symmetrically, every current
\(\rho_h\) occurrence lies before \(\gamma\), while \(q^+\) lies after it,
proving the right assertion. \(\square\)

For an inherited packet with shared jump labels, (3.4) remains the number
of casualty **addresses**, but distinct addresses can have equal target
values when advancing one marginal adds a coordinate already supplied by
the opposite bank.  The exact-width diagonal antichain on each shore
remains valid, but (3.4) and every numerical consequence using distinctness
must either be restricted to the fresh-bank case or recomputed on the
collision quotient.

At lower-compiler width at most \(h\), each shore contributes
\(h(h-1)/2\) crossing casualties.  At exact width \(h\), each contributes
the \(h-1\) diagonal values.  Those diagonal values are pairwise
incomparable: a step exchanges one fresh exterior-bank coordinate for one
fresh central-bank coordinate.  Thus even the fixed-width casualty bank
has width \(2h-2\).

The target-side intersections of the two complete grids are

\[
\begin{aligned}
 G_L&=(X_R-\{x_R\})+\{q^-,\lambda_1\}
       +{\bf1}_{j=1}(B-\{x_R\}),\\
 G_R&=(X_L-\{x_L\})+\{\rho_h,q^+\}
       +{\bf1}_{s=h}(B-\{x_L\}).                       \tag{3.5}
\end{aligned}
\]

Consequently

\[
G_L\cap G_R=
\begin{cases}
 \varnothing,&j>1, s<h,\\
 X_L-\{x_L\},&j=1, s<h,\\
 X_R-\{x_R\},&j>1, s=h,\\
 B-\{x_L,x_R\},&j=1, s=h.
\end{cases}                                             \tag{3.6}
\]

Thus even a single nonzero target-side anchor for both shores is not
uniformly available.  As in (2.3), this is not a full common-Q criterion.

## 4. First obstruction and the positive rail

For \(h=2\), the four smallest left-seam values are

\[
 Z,\quad Z+d^-_1,\quad Z+\lambda_2,\quad
 Z+d^-_1+\lambda_2,                                   \tag{4.1}
\]

where

\[
                         Z=(B-\{x_R\})+\{q^-,\lambda_1\}.
\]

They form a Boolean diamond.  The middle two overlap and are incomparable,
while every natural child address contains \(\alpha\).  This is the first
exact obstruction to a laminar casualty theorem.

The nonlaminarity does not obstruct an unconstrained common source for the
OR rows.

### Lemma 4.1 (Ferrers rail)

Let

\[
 L_1\supseteq\cdots\supseteq L_p,qquad
 P_1\subseteq\cdots\subseteq P_q.
\]

The source word

\[
 L_1\cup P_1,\ldots,L_p\cup P_1,
 L_p\cup P_2,\ldots,L_p\cup P_q                       \tag{4.2}
\]

realizes every \(L_a\cup P_b\), at interval
\([a,p+b-1]\).

#### Proof

The union of positions \(a,\ldots,p\) is \(L_a\cup P_1\); adjoining the
next \(b-1\) positions enlarges exactly the second marginal to \(P_b\).
\(\square\)

In particular, one literal copy of the parent word \(W_h\), with its old
interval assignment, realizes both complete casualty grids in one source
and passes their exact OR-row reconstruction.  It is an actual common-Q
host only if all of its letters also pass the ambient point caps and every
owner/mixed guard; those are separate screens.

## 5. No bounded physical sidecar

### Theorem 5.1 (standalone length lower bound)

For a fresh pairwise-disjoint packet, if no unaffected exterior cell
realizes a jump casualty and a standalone \(L\)-letter sidecar must realize
all \(5h^2+2h\) distinct values, then

\[
 L\ge
 \left\lceil\frac{\sqrt{1+8(5h^2+2h)}-1}{2}\right\rceil
 =\Omega(h).                                            \tag{5.1}
\]

#### Proof

An \(L\)-letter word has only \(L(L+1)/2\) nonempty interval addresses.
Apply Theorem 3.2. \(\square\)

There is also a sharper structural cut.

### Proposition 5.2 (separated-marginal frozen-separator cut)

Assume the repair architecture certifies every alternate witness either by
one whole exported left-prefix signature or by one whole exported
right-tail signature; mixed letters encoding both marginals at once are
forbidden.  Restrict the left grid to \(h\)
suffix signatures and \(h\) prefix signatures.  Because \(\alpha\) is a
fixed forbidden separator, an alternate interval lies wholly on one side.
Let \(R\) be the tail signatures exported to the right side and \(C\) the
prefix signatures exported to the left.  Covering every grid pair says
that \(R\cup C\) is a vertex cover of \(K_{h,h}\).  Therefore

\[
                              |R|+|C|\ge h.             \tag{5.2}
\]

If \(c_L,c_R\) new letters are the only source of these signatures, then

\[
{c_L+1\choose2}+{c_R+1\choose2}\ge h,                 \tag{5.3}
\]

and hence

\[
 c_L+c_R\ge
 \left\lceil\frac{\sqrt{8h+1}-1}{2}\right\rceil.       \tag{5.4}
\]

#### Proof

Index a restricted target by its tail signature \(a\) and prefix signature
\(b\).  A witness avoiding the frozen \(\alpha\) cannot use letters on
both sides of it.  A left-side witness therefore requires signature \(b\)
to have been exported left, while a right-side witness requires signature
\(a\) to have been exported right.  Thus every edge \((a,b)\) of
\(K_{h,h}\) has an endpoint in \(R\cup C\).  The minimum vertex cover of
\(K_{h,h}\) has size \(h\), proving (5.2).  A block of \(c\) new letters
has at most \({c+1\choose2}\) nonempty interval signatures, giving (5.3).
For fixed \(c_L+c_R\), the left side of (5.3) is maximized by concentrating
all letters on one side, which gives (5.4). \(\square\)

Equation (5.2) is an exact architecture-local
transport cut: an ordinary exterior sector can pass it by exporting
a full row or column rail, while an \(O(1)\)-letter append-only repair
cannot do so uniformly.

For the plateau q1 antichain, the analogous retained-scaffold statement is
even simpler.  A family of newly free addresses partitioned into \(c\)
inclusion chains can host at most \(c\) of the \(3h\) distinct equal-rank
targets.  A terminal \(c\)-letter append supplies \(c\) such endpoint
chains, so it needs \(c\ge3h\).  For \(t\) one-cell seam credits, cells
using two distinct credits add at most \({t\choose2}\) further antichain
addresses to the two fan addresses per credit: one inclusion chain contains
at most one member of a fixed-rank antichain, and a fixed unordered pair of
credits determines at most one two-partial-endpoint cell of that rank.  The proof-safe general
bound is therefore

\[
 3h\le2t+{t\choose2}=\frac{t(t+3)}2,
 \qquad
 t\ge\left\lceil\frac{\sqrt{24h+9}-3}{2}\right\rceil. \tag{5.5}
\]

If cross-credit cells are forbidden, the sharper \(t\ge\lceil3h/2\rceil\)
follows.  These are retained-old-scaffold no-gos, not global Pascal
impossibilities.

## 6. Exact surviving gate

For a proposed global child, make a bipartite occurrence graph whose left
vertices are:

1. the plateau old-q1 antichain and every other selected old target whose
   natural interval meets \(Z_\beta\); and
2. the two jump casualty grids (or only their selected compiler rows).

A target is adjacent to a child interval only if the interval avoids every
fresh coordinate omitted by the target and its frozen-prefix screened cap
can reconstruct that target.  Select distinct interval vertices, add those
rows to the full owner/terminal/mixed row bank, and apply relative maximal
erosion once.

The exact remaining positive hypothesis is:

> the occurrence graph has a matching leaving only \(O(1)\) targets, and
> the selected rows pass one simultaneous frozen-prefix maximal-word test.

The Ferrers rail proves the OR rows are jointly realizable when an
already-budgeted parent-shaped ordinary sector is available; ambient caps
and mixed guards must still pass.  In the fresh-bank case, Theorems 3.2 and
5.1 prove this rail cannot be replaced by a standalone \(O(1)\)-letter
local sidecar.  On inherited shared-bank packets, the same conclusion may
be drawn only after recomputing the distinct-value collision quotient.

Finally, the algebraic carry itself has a separate sharp residence horizon.
Starting from disjoint depth-\(h_0\) banks, all inherited shared labels are
resident only through \(t\le h_0\) deadline jumps.  Beyond that point the
construction also needs a shared-bank rebase/rethread.  Thus the complete
bounded-defect recurrence has two genuinely distinct global gates:

\[
 \boxed{\text{ordinary-sector transport matching/common-Q}}
 \quad+\quad
\boxed{\text{shared-bank residence regeneration}}.
\]

The plateau statements and the jump address identity hold for every
standard inherited packet.  The distinct-value count, Boolean-diamond
lower bound, standalone length bound, and separated-marginal cut were
proved here for the fresh pairwise-disjoint packet.  Repeated use is valid
only through the residence horizon and, for numerical sidecar bounds, only
after quotienting target collisions caused by shared bank labels.
