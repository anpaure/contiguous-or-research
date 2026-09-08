# Coordinate automorphisms of the Dyck family and exhaustive conjugate minimax

Date: 2026-07-26

Method: pure mathematics only.  No finite search, solver, program, or web
input is used.

## 0. Result and exact scope

Let \(\mathcal D_s\subseteq\binom{[2s]}s\) be the family of Dyck
\(s\)-subsets.  Write \(C_n=\operatorname {Cat}_n\) and
\(C(z)=\sum_{n\ge0}C_nz^n\), so \(C(z)=1+zC(z)^2\).  Put

\[
 H_s=\left\langle(2i\ 2i+1):1\le i<s\right\rangle.   \tag{0.1}
\]

Then, for every \(s\ge1\),

\[
             \boxed{\operatorname {Aut}_{S_{2s}}(\mathcal D_s)=H_s
                    \cong C_2^{s-1}.}                 \tag{0.2}
\]

There are no small-rank exceptions: the groups are trivial at \(s=1\),
and at \(s=2\) both sides equal \(\langle(2\ 3)\rangle\).

The proof uses only one-coordinate incidence numbers.  Their fibres are
exactly

\[
 \{1\},\quad \{2i,2i+1\}\ (1\le i<s),\quad \{2s\}, \tag{0.3}
\]

and the corresponding values are strictly decreasing.

Let \(F_s\) be the canonical anchored MSW factor.  Among every covariant
coordinate conjugate of this fixed seed which is again anchored at
\(\mathcal D_s\), the all-block swap

\[
 w_s=\prod_{i=1}^{s-1}(2i\ 2i+1)                    \tag{0.4}
\]

is therefore minimax-optimal for the first-return-resolved first-target
objective.  This is not merely optimal inside a guessed swap grammar:
(0.2) proves that the grammar contains every possible covariant coordinate
conjugator.

The exact minimax value is

\[
 \boxed{
 \min_{\pi\in\operatorname {Aut}(\mathcal D_s)}
 \max_{j,x}Q_\pi(j,x)
 =
 \begin{cases}
 1,&s=1,2,\\
 R_{s-1},&s\ge3,
 \end{cases}}                                         \tag{0.5}
\]

where

\[
 \sum_{n\ge0}R_nz^n
   =\frac1{1-z^2C(z)^2}
   =\frac{C(z)^2}{2C(z)-1}.                           \tag{0.6}
\]

Here \(Q_\pi(j,x)\) is the number of roots in original first-return class
\(j\) whose conjugated row first inserts physical coordinate \(x\).
The same value remains minimax if the admissible class is enlarged to
exact factors obtained by choosing, independently on each row, a row from
the coordinate-conjugate library; exact legality of such a rowwise choice
is a separate constraint, but the lower bound is pointwise and the global
full swap is legal.
Moreover

\[
                     R_n\sim\frac49C_n,
 \qquad \frac{R_{s-1}}{C_s}\longrightarrow\frac19.  \tag{0.7}
\]

The scope is load-bearing.  If “every exact seed” means that the base
factor itself may be arbitrary before conjugation, then the identity
conjugator is allowed and the problem is exactly optimization over all
exact factors.  Neither (0.2) nor (0.5) proves that larger statement.

## 1. Exact coordinate incidences

Identify a Dyck word with its up-step positions.  Equivalently,

\[
 \mathcal D_s=
 \left\{\{p_1<\cdots<p_s\}:p_i\le2i-1\right\}.       \tag{1.1}
\]

For \(x\in[2s]\), define its incidence degree

\[
                    \nu_s(x)=|\{P\in\mathcal D_s:x\in P\}|.       \tag{1.2}
\]

Put

\[
 B_0=\{1\},\qquad B_i=\{2i,2i+1\}\ (1\le i<s),
 \qquad B_s=\{2s\}.                                  \tag{1.3}
\]

### Theorem 1.1 (complete incidence flag)

The function \(\nu_s\) is constant, with value \(A_i\), on \(B_i\), and

\[
 A_i-A_{i+1}=C_iC_{s-i-1}>0
                 \qquad(0\le i<s).                  \tag{1.4}
\]

Equivalently,

\[
                  A_i=\sum_{t=i}^{s-1}C_tC_{s-1-t},
                  \qquad0\le i\le s,                \tag{1.5}
\]

where the empty sum \(A_s\) is zero.  Thus

\[
                         A_0>A_1>\cdots>A_s.          \tag{1.6}
\]

#### Proof

For \(1\le i<s\), the height of a Dyck path immediately before position
\(2i\) is odd and nonnegative, hence at least one.  Interchanging the
two steps preserves Dyckness: equal steps do nothing, \(01\mapsto10\)
raises the intermediate height, and \(10\mapsto01\) lowers it by two but
not below zero.  Therefore

\[
                         \nu_s(2i)=\nu_s(2i+1)=A_i.   \tag{1.7}
\]

For \(1\le i<s\), compare positions \(2i+1\) and \(2i+2\).  Swapping the
local patterns maps every Dyck word with \(01\) there to one with \(10\)
there.  The reverse swap is valid unless the height after \(2i\) steps is
zero.  Words having equal bits cancel from the incidence difference, so
this is a bijection between all nonexceptional contributions.  In the
exceptional case the word factors uniquely as

\[
                   U\,10\,V,\qquad
                   U\in\mathcal D_i,\quad
                   V\in\mathcal D_{s-i-1}.            \tag{1.8}
\]

There are \(C_iC_{s-i-1}\) such words.  This proves (1.4) for the
interior indices.  At \(i=0\), every Dyck word contains coordinate one,
and those omitting coordinate two are exactly \(10V\),
\(V\in\mathcal D_{s-1}\), giving \(C_0C_{s-1}\).  At the right endpoint,
coordinate \(2s\) never occurs and the same factorization gives
\(A_{s-1}=C_{s-1}C_0\).  Thus (1.4) holds throughout.

Since \(A_s=0\), summing (1.4) gives (1.5).  Strictness is immediate.
\(\square\)

No pair-incidence or higher-incidence invariant is needed: (1.6) already
reconstructs every block in (1.3) intrinsically from the set system.

## 2. The coordinate automorphism group

### Theorem 2.1

For every \(s\ge1\), equation (0.2) holds.

#### Proof

Every coordinate permutation preserving \(\mathcal D_s\) setwise
preserves the incidence function (1.2).  The strict flag (1.3)--(1.6)
therefore forces it to fix each \(B_i\) setwise.  It fixes coordinates
\(1,2s\), and on every other block it can only apply the transposition
\((2i\ 2i+1)\).  Hence

\[
             \operatorname {Aut}(\mathcal D_s)\le H_s.             \tag{2.1}
\]

The local-height argument proving (1.7) proves more: each generator
\((2i\ 2i+1)\) sends every Dyck word to a Dyck word.  The generators have
disjoint supports and may be chosen independently, so \(H_s\) is contained
in the automorphism group.  \(\square\)

## 3. Why this exhausts coordinate-conjugate anchored seeds

Let \(F_s(P)\) denote the canonical rooted path from \(P\) to
\([2s]\setminus P\).  For a coordinate permutation \(\pi\), its covariant
conjugate, when defined on the original root family, is

\[
 G_\pi(P)=\pi F_s(\pi^{-1}P),
                         \qquad P\in\mathcal D_s.     \tag{3.1}
\]

Coordinate relabelling preserves every lower state, upper colour,
Johnson adjacency, and complementary endpoint.  Hence (3.1) is an exact
anchored \(\mathcal D_s\)-factor whenever
\(\pi\mathcal D_s=\mathcal D_s\).

Conversely, the initial-port set of the covariantly conjugated canonical
factor is \(\pi\mathcal D_s\).  If it is again the anchored port set
\(\mathcal D_s\), then necessarily

\[
                         \pi\mathcal D_s=\mathcal D_s.              \tag{3.2}
\]

Theorem 2.1 now gives \(\pi\in H_s\).  Thus

\[
 \boxed{\{\text{covariant coordinate conjugates of }F_s
       \text{ anchored at }\mathcal D_s\}
       =\{G_h:h\in H_s\}.}                           \tag{3.3}
\]

This is the step which upgrades an \(H_s\)-minimax theorem from a grammar
statement to an exhaustive coordinate-conjugacy theorem.

There is a different contravariant symmetry: coordinate reversal followed
by reversing the path in time acts on roots by reverse--complement.  It
exchanges first-insertion data with reflected last-deletion data and is not
an additional covariant coordinate automorphism in (3.3).

## 4. The resolved minimax objective

Let

\[
 \mathcal F_{s,j}=\{P\in\mathcal D_s:
              \text{the first return of }P\text{ is at }2j\}.      \tag{4.1}
\]

For an anchored factor \(G\), let \(b_1^G(P)\) be the first inserted
coordinate on its row rooted at \(P\), and put

\[
 Q_G(j,x)=|\{P\in\mathcal F_{s,j}:b_1^G(P)=x\}|,
 \qquad
 L(G)=\max_{j,x}Q_G(j,x).                             \tag{4.2}
\]

For \(h\in H_s\), abbreviate \(Q_h=Q_{G_h}\).

Encode a Dyck word uniquely as

\[
                  1\,b_1b_2\cdots b_{s-1}\,0,
                  \qquad |b_i|=2,                    \tag{4.3}
\]

and map

\[
 11\mapsto U,\quad00\mapsto D,\quad
 01\mapsto L_0,\quad10\mapsto L_1.                  \tag{4.4}
\]

This is a bijection with two-coloured Motzkin excursions of length
\(s-1\).  The group \(H_s\) changes only the two colours of horizontal
steps; it fixes the uncoloured Motzkin skeleton.

Let \(R_n\) count excursions having no ground-level horizontal step of
either colour.  A ground excursion is a sequence of elevated blocks,
each with generating function \(z^2C(z)^2\).  Hence (0.6) follows.
More generally the three exact ground-interval generating functions are

\[
 \frac1{1-z^2C(z)^2}=R(z),\qquad
 \frac1{1-z-z^2C(z)^2}=C(z),\qquad
 \frac1{1-2z-z^2C(z)^2}=C(z)^2.                    \tag{4.5}
\]

They respectively forbid both ground-horizontal colours, forbid one
specified colour, or forbid neither.  All identities follow directly
from \(C(z)=1+zC(z)^2\).

## 5. Universal lower bound for every coordinate conjugate

### Theorem 5.1

For \(s\ge3\) and every \(h\in H_s\),

\[
                         Q_h(s,2s)\ge R_{s-1}.         \tag{5.1}
\]

#### Proof

Take a root \(P\) whose two-coloured Motzkin excursion has no ground
horizontal step.  There are \(R_{s-1}\) such roots, and each lies in
\(\mathcal F_{s,s}\).  Because \(h^{-1}\) only changes horizontal
colours, \(h^{-1}P\) also has no ground horizontal step and hence also
has first-return class \(s\).  Its canonical first target is \(2s\).
By (3.1),

\[
 b_1^{G_h}(P)=h\bigl(b_1^{F_s}(h^{-1}P)\bigr)=h(2s)=2s.           \tag{5.2}
\]

Thus all \(R_{s-1}\) chosen roots lie in the same resolved cell
\((s,2s)\).  \(\square\)

The same statement survives arbitrary probability mixtures of global
coordinate conjugates: the expected load of this one cell is still at
least \(R_{s-1}\).  In fact it is pointwise stronger.  One may choose a
possibly different \(h_P\in H_s\) on every root and use the row
\(G_{h_P}(P)\).  For each of the \(R_{s-1}\) no-ground-horizontal roots,
the calculation (5.2) still gives first target \(2s\).  Such arbitrary
rowwise choices need not form an exact factor, but every rowwise choice
which does satisfy the exact resource ledgers inherits the same lower
bound.  Since the global full swap is one legal member, its value is also
minimax over the larger class of legal exact rowwise selections from the
coordinate-conjugate row library.

## 6. The all-block swap attains the bound

Let \(w_s\) be (0.4).  It exchanges the two horizontal colours in every
Motzkin time slot.  In the encoding (4.3)--(4.4), the original
first-return class is the time of the first ground \(L_0\), with the
value \(s\) if there is none.  After \(w_s\), the analogous time is the
time of the original first ground \(L_1\).  Let \(M^{(s)}_{jk}\) count
roots whose first ground
\(L_0\)-horizontal occurs at time \(j\), or never when \(j=s\), and whose
first ground \(L_1\)-horizontal occurs at time \(k\), or never when
\(k=s\).  Then

\[
 M^{(s)}_{jk}=
 \begin{cases}
 0,&j=k<s,\\[1mm]
 R_{\min(j,k)-1}C_{|j-k|-1}C_{s-\max(j,k)},
      &j\ne k,\ \max(j,k)<s,\\[1mm]
 R_{j-1}C_{s-j-1},&j<s,\ k=s,\\[1mm]
 R_{k-1}C_{s-k-1},&k<s,\ j=s,\\[1mm]
 R_{s-1},&j=k=s.
 \end{cases}                                          \tag{6.1}
\]

The corresponding physical target is

\[
 \lambda_s(k)=
 \begin{cases}
 2k+1,&k<s,\\
 2s,&k=s.
 \end{cases}                                          \tag{6.2}
\]

More precisely,

\[
 Q_{w_s}\bigl(j,\lambda_s(k)\bigr)=M^{(s)}_{jk},
 \qquad Q_{w_s}(j,x)=0
 \quad\text{for }x\notin\lambda_s([s]).              \tag{6.2a}
\]

Indeed, the canonical seed inserts coordinate \(2k\) from a root of
first-return class \(k\); conjugation by \(w_s\) sends this to \(2k+1\)
for \(k<s\) and fixes \(2s\).

### Theorem 6.1

For \(s\ge3\), every entry of (6.1) is at most \(R_{s-1}\), and equality
holds at \((s,s)\).  Consequently

\[
                             L(G_{w_s})=R_{s-1}.       \tag{6.3}
\]

#### Proof

The ground-atom decomposition gives (6.1).  A ground interval of length
\(t\) with both horizontal colours forbidden is counted by \(R_t\); with
one prescribed colour forbidden it is counted by \(C_t\); and with no
colour forbidden it is counted by \(C_{t+1}\).  Splitting immediately
before and after the first specified ground horizontals yields exactly
the five cases displayed in (6.1).

For an interior entry with \(j<k<s\), put

\[
 a=j-1,\qquad b=k-j-1,\qquad c=s-k.                  \tag{6.4}
\]

An object counted by \(R_aC_bC_c\) consists of a sequence \(A\) of
non-singleton primitive Dyck components and arbitrary Dyck words \(B,D\)
of semilengths \(b,c\).  Send it to

\[
                             A\cdot1(BD)0.             \tag{6.5}
\]

The appended component has semilength \(b+c+1\ge2\), so this is a
sequence of non-singleton primitive components of total semilength
\(a+b+c+1=s-1\).  Its last primitive component is \(1(BD)0\); because
the integers \(b,c\) are fixed by the matrix cell, cutting its interior
after \(2b\) symbols recovers \(B,D\), and the preceding components
recover \(A\).  The map is therefore injective.  The case \(j>k\) is
symmetric.

For a boundary entry write it as \(R_aC_b\), where \(a+b=s-2\).
If \(b\ge1\), map \((A,B)\) to \(A\cdot1B0\).  The appended primitive
has semilength at least two and the map is injective.  If \(b=0\), then
\(a=s-2\).  For \(s=3\) the domain is empty because \(R_1=0\).  For
\(s\ge4\), every word \(A\) counted by \(R_{s-2}\) is nonempty, and
\(A\mapsto1A0\) injects it as one non-singleton primitive component of
semilength \(s-1\).  Thus every boundary entry is also at most
\(R_{s-1}\).  The diagonal entries below \((s,s)\) are zero, while the
corner entry is exactly \(R_{s-1}\).  \(\square\)

Combining Theorems 2.1, 5.1, and 6.1 proves (0.5) for \(s\ge3\).
At \(s=1\) the unique cell has size one.  At \(s=2\), \(R_1=0\), but the
two off-diagonal cells under the full swap each have size one; the minimax
value is one.

For completeness, write \(\Phi(u)=u^2/(2u-1)\).  At the Catalan
singularity,

\[
 C(z)=2-2\sqrt{1-4z}+O(1-4z),\qquad \Phi'(2)=\frac49.
\]

Because \(R(z)=\Phi(C(z))\), it follows that

\[
 R(z)=\frac43-\frac89\sqrt{1-4z}+O(1-4z).
\]

The standard coefficient estimate for the square-root singularity gives
\(R_n\sim(4/9)C_n\).  Since \(C_{s-1}/C_s\to1/4\), equation (0.7)
follows with the claimed constant \(1/9\).

## 7. What “every coordinate-conjugate seed” does and does not mean

The exhaustive positive statement is:

> Fix the canonical anchored seed \(F_s\).  Among every global coordinate
> permutation whose covariant image is again anchored at the same Dyck
> port family, the all-block swap minimizes the largest resolved
> first-target cell, with value (0.5).

This includes every coordinate conjugator, whether or not it was first
described through the Motzkin grammar, because Theorem 2.1 proves that
there are no others.

It does **not** prove any of the following stronger statements.

1. Optimality among arbitrary anchored exact factors.  If the base seed
   \(E\) is allowed to vary, the identity conjugator already includes
   every such \(E\).
2. Optimality for weak, unanchored Dyck transversals, where a selected
   Dyck state may lie internally rather than at the port.
3. Optimality after general ownership-component switches or splices whose
   rows leave the coordinate-conjugate row library.  Rowwise selections
   that stay inside that library are covered by the pointwise strengthening
   after Theorem 5.1, provided their exact legality is checked separately.
4. A raw physical-cap bound.  After the source first-return label is
   forgotten, every exact factor still has the forced first-insertion
   load \(C_{s-1}\) at coordinate \(2s\).
5. A favourable two-sided or multidepth carrier theorem with background.

Thus the global coordinate-conjugacy lane is genuinely exhausted, while
the arbitrary exact-factor lane remains open.
