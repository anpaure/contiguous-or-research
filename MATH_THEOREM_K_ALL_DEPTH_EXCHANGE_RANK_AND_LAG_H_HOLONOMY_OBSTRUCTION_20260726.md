# All-depth exchanges do not by themselves compile the MSW owner-star lift: lag-\(H\) holonomy and an unbounded-rank Markov obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad N=N_H=\binom{2m}{M},
 \qquad MN=(1+o(1))W,
\tag{0.1}
\]

with \(2H<M\).  Take as audited inputs the exact MSW owner-star lift,
the phasewise triangle/directed-cycle exchanges, the checkerboard and
higher-cube all-depth identities, and the common-core tight-path
compiler.

This note proves the following statewise obstruction, which is distinct
from component colouring.

1.  A proposed grouping of middle clones at one root has an exact
    nonabelian lag-\(H\) holonomy.  If
    \(J_i\in\binom UH\) are its cyclic middle windows and
    \(x_i=J_i\setminus J_{i+1}\), then the insertion permutation must be

    \[
       \sigma(x_i)=x_{i+H}.
    \tag{0.2}
    \]

    Consequently \(\sigma\) must belong to the conjugacy class of the
    rotation \(i\mapsto i+H\) on \(\mathbb Z_M\): it has exactly
    \(g=\gcd(M,H)\) cycles, all of length \(M/g\).  This condition is
    invisible to separate clone Hall matchings.

2.  Every triangle, directed-cycle, quartet, or higher-cube exchange is
    an integer-kernel move for the complete phase-refined all-depth load
    matrix.  Hence such exchanges preserve every target multiplicity,
    every hole set, every collision energy, and every floor excess.
    They can regroup an already integral good-load table, but they cannot
    turn the ungrouped clone-Hall point into an integral table or improve
    a bad load vector.

3.  More strongly, fix any integer \(R\ge2\).  There is a full frame
    fibre with two literal one-frame-at-every-top tables, identical at every
    phase and every depth, such that both tables are isolated under the
    library consisting of

    * every fixed-core directed-cycle exchange, of arbitrary cycle
      length; and
    * every coherent common-base cube exchange of placeholder rank at
      most \(R\).

    The construction places \(N-o(N)\) tops in disjoint
    \((R+1)\)-cube gadgets and gives the remaining tops common frames.
    Every selected column has genuine nested
    chronology and every one of its middle incidences has an MSW
    owner-star certificate.  Thus local MSW certification does not
    remove the obstruction.

4.  If the only escape is to discard or replace a complete top frame in
    every trapped gadget, at least

    \[
       \left(2^{-(R+1)}-o(1)\right)N
    \tag{0.3}
    \]

    top frames, hence

    \[
       \left(2^{-(R+1)}-o(1)\right)MN
       =\left(2^{-(R+1)}-o(1)\right)W
    \tag{0.4}
    \]

    phase incidences, are exposed.  Therefore no fixed-rank version of
    this move library gives a universal \(o(W)\)-repair compiler.  To
    reduce this particular full-frame replacement toll to \(O(N)\), one
    needs

    \[
                         R\ge \log_2 M-O(1).
    \tag{0.5}
    \]

The theorem does **not** prove that a growing-rank library fails, nor
that a temporary frame can never be used catalytically and recycled.  It
also does not by itself lower-bound the number of output word components:
both isolated endpoints already consist of one legal frame per top and
therefore compile into \(O(N)\) blocks.  What it closes is the proposed
bounded-rank Markov route from local owner-star witnesses to a universal
global lag-\(H\) braid.

## 1. Exact lag-\(H\) holonomy

Fix a promotion root \(A\), put \(U=A^c\), and suppose a repaired cyclic
middle deck has been completed to

\[
                         J_i\in\binom UH,
                         \qquad i\in\mathbb Z_M.
\tag{1.1}
\]

Assume successive windows differ by one exchange and that the deleted
singletons

\[
                         x_i:=J_i\setminus J_{i+1}
\tag{1.2}
\]

are distinct and exhaust \(U\).  Since the deck closes, the inserted
singletons

\[
                         y_i:=J_{i+1}\setminus J_i
\tag{1.3}
\]

also exhaust \(U\).  Define the insertion permutation

\[
                         \sigma(x_i)=y_i.
\tag{1.4}
\]

### Theorem 1.1 (nonabelian rotor criterion)

The deck (1.1) comes from one labelled cyclic frame, with \(J_i\) its
cyclic \(H\)-windows in the chosen orientation, if and only if

\[
                         y_i=x_{i+H}
                         \qquad(i\in\mathbb Z_M).
\tag{1.5}
\]

Equivalently, if \(\xi(i)=x_i\) and
\(\rho_H(i)=i+H\), then

\[
                         \sigma=\xi\rho_H\xi^{-1}.
\tag{1.6}
\]

In particular every legal deck has

\[
 \operatorname{type}(\sigma)
 =\left(M/g,\ldots,M/g\right),
 \qquad g=\gcd(M,H).
\tag{1.7}
\]

#### Proof

For a cyclic frame \((x_0,\ldots,x_{M-1})\), its \(i\)-th
\(H\)-window loses \(x_i\) and gains \(x_{i+H}\) on advancing one
phase.  This gives (1.5), hence (1.6).

Conversely, (1.2), (1.3), and (1.5) give

\[
                         J_{i+1}=J_i-x_i+x_{i+H}.
\tag{1.8}
\]

The set

\[
                         K_i=\{x_i,x_{i+1},\ldots,x_{i+H-1}\}
\tag{1.9}
\]

satisfies the same recurrence.  More explicitly, \(x_k\) is inserted
at transition \(k-H\), deleted at transition \(k\), and no other
transition changes its membership.  Hence it belongs exactly to
\(J_{k-H+1},\ldots,J_k\).  In particular
\(J_0=\{x_0,\ldots,x_{H-1}\}=K_0\).  Induction in (1.8) gives
\(J_i=K_i\) for every \(i\).  Thus the cyclic
word \((x_0,\ldots,x_{M-1})\) realizes the deck.  Finally a rotation by
\(H\) on \(M\) points has \(g\) cycles of length \(M/g\), proving
(1.7). \(\square\)

This is stronger than the scalar conditions
\(|J_i\cap J_{i+1}|=H-1\) and balanced use of each label.  A clone table
may satisfy both scalar conditions while its permutation (1.4) has the
wrong cycle type.  No choice of a cyclic ordering can repair that table
without changing at least one assigned clone.

## 2. Kernel moves cannot supply feasibility or energy descent

Let \(\mathsf A\) be the matrix whose columns are literal common-order
frame columns and whose rows record the top together with every retained
phase/target/depth incidence.  For a table \(z\), write

\[
                         b=\mathsf A z.
\tag{2.1}
\]

The audited phasewise cycle and cube identities say exactly that every
allowed exchange vector \(h\) obeys

\[
                         \mathsf A h=0.
\tag{2.2}
\]

### Proposition 2.1 (fibre and energy invariance)

Along every sequence of the audited load-neutral exchanges, the vector
\(b\) is fixed.  Consequently, at every depth, the following are fixed:

1. every individual physical target multiplicity;
2. the set and number of missing targets;
3. \(\sum_S\binom{b_S}{2}\);
4. every factorial-floor correction obtained by subtracting a fixed
   linear baseline; and
5. every weighted sum of these quantities across depths.

#### Proof

Equation (2.2) gives (2.1) unchanged after one move and hence after any
sequence.  Each listed quantity is a function of \(b\) alone. \(\square\)

Thus the exact role of these exchanges is restricted.  They may connect
different nonnegative integral decompositions of one already feasible
all-depth vector \(b\).  Separate clone-Hall matchings give a point in a
projection of this system; they do not give a nonnegative integral
preimage under \(\mathsf A\).  Kernel moves cannot prove that the fibre

\[
             \{z\in\mathbb Z_{\ge0}^{\mathcal E}:\mathsf A z=b\}
\tag{2.3}
\]

is nonempty.

The moving-hole two-top transfer is not covered by this proposition: it
has the explicit nonzero lower-depth action
\(e_{X_q}-e_{Y_q}\).  It is therefore a possible energy move, but it
does not preserve an arbitrary common nested tag schedule and no dense
packing theorem for it is presently available.

## 3. The rank-\(r\) trap

Fix \(r\ge3\).  Take an \((M-r)\)-set \(C\), disjoint label pairs

\[
                         \{a_{j,0},a_{j,1}\},
                         \qquad 1\le j\le r,
\tag{3.1}
\]

and the \(2^r\) tops

\[
 U_\varepsilon=C\cup
 \{a_{1,\varepsilon_1},\ldots,a_{r,\varepsilon_r}\},
 \qquad \varepsilon\in\{0,1\}^r.
\tag{3.2}
\]

Put the placeholders \(A_1,\ldots,A_r\) in distinct gaps of one cyclic
word on \(C\cup\{A_1,\ldots,A_r\}\), and let

\[
                         \gamma=(A_1A_2\cdots A_r).
\tag{3.3}
\]

Let \(\pi^1_\varepsilon\) and \(\pi^\gamma_\varepsilon\) be the two
specialized frames.  Define the two checkerboard tables

\[
 T_0(\varepsilon)=
 \begin{cases}
 \pi^1_\varepsilon,&|\varepsilon|\text{ even},\\
 \pi^\gamma_\varepsilon,&|\varepsilon|\text{ odd},
 \end{cases}
 \qquad
 T_1(\varepsilon)=
 \begin{cases}
 \pi^\gamma_\varepsilon,&|\varepsilon|\text{ even},\\
 \pi^1_\varepsilon,&|\varepsilon|\text{ odd}.
 \end{cases}
\tag{3.4}
\]

Fix throughout one common deleted phase, if repaired rings are wanted,
and one common nested phase-tag schedule.  Identity (3.5) is phasewise
before these restrictions and therefore survives them.

The audited cube derivative gives, for every phase \(s\) and every
proper interval length \(\ell\),

\[
 \sum_\varepsilon(-1)^{|\varepsilon|}
 \left(v^1_\varepsilon(s,\ell)
      -v^\gamma_\varepsilon(s,\ell)\right)=0.
\tag{3.5}
\]

Hence \(T_0,T_1\) have identical phase-refined all-depth loads.

### Lemma 3.1 (no directed-cycle move is supported in one trap)

Every fixed-core directed-cycle exchange whose touched tops all belong
to (3.2) is a four-cycle on a two-dimensional coordinate face.
Consequently neither endpoint in (3.4) admits such a move.

#### Proof

A directed-cycle exchange has tops

\[
                         C'\cup\{z_i,z_{i+1}\}
\tag{3.6}
\]

for one common \((M-2)\)-core \(C'\).  Thus every touched top contains
\(C'\), and only two labels of that top lie outside \(C'\).  Inside the
binary product (3.2), at most two coordinate families can therefore
vary; every other selected label belongs to \(C'\).  The simple cycle is
then a cycle in a two-dimensional cube, hence the unique four-cycle.

On that face, (3.4) alternates between the identity and the long cycle
\(\gamma\).  At least one of the \(r-2\) fixed placeholder labels is
moved to a different core gap by \(\gamma\).  Therefore the restrictions
of the selected frames to the common \((M-2)\)-core do not agree, which
is precisely the audited quartet nonapplicability criterion.  (For
\(r=3\), there is one such fixed label.) \(\square\)

### Lemma 3.2 (no proper coherent subcube move is supported)

No coherent common-base cube exchange of dimension \(d<r\) is
applicable to either endpoint in (3.4).

#### Proof

Any \(d\)-cube in (3.2) fixes \(r-d\ge1\) selected placeholder labels.
The two frame types in (3.4) restrict differently to that fixed common
core because the long cycle \(\gamma\) moves every placeholder to a
different prescribed gap.  A physical common-base cube move requires
the fixed-core restrictions to coincide. \(\square\)

The first coherent cube move capable of directly crossing the trap has
rank \(r\) and touches all \(2^r\) tops.

## 4. Dense global isolation for every fixed maximum rank

### Theorem 4.1 (cycle-plus-cube Markov obstruction)

Fix \(R\ge2\), and put \(r=R+1\).  For all sufficiently large \(m\),
there are two tables with top margin one on every one of the \(N\) tops,
lying in one exact phase-refined all-depth fibre, such
that neither table admits

1. any fixed-core directed-cycle exchange, of any length; or
2. any coherent common-base cube exchange of dimension at most \(R\).

The two tables differ on \(N-o(N)\) tops.

#### Proof

Partition the ground labels into \(m\) fixed pairs.  For each fixed
full/empty/single pair pattern, the choices in the single pairs form a
Boolean cube.  Apart from \(o(N)\) tops, there are at least \(r\) single
pairs.  Choose \(r\) of them and partition the choice cube into disjoint
coordinate \(r\)-cubes.  Install (3.4) on every resulting gadget.
On the remaining \(o(N)\) tops install the same independently chosen
frame in both tables.

Choose the common cyclic positional word of each gadget independently
and uniformly, subject to putting its \(r\) placeholders in distinct
core gaps.  Lemmas 3.1 and 3.2 exclude every allowed move contained in
one gadget.

It remains to exclude moves meeting more than one gadget.  Consider
first a directed cycle of length \(t\).  Its tops share an
\((M-2)\)-core and each has two labels outside it.  One rank-\(r\)
gadget can contribute at most four tops to such a simple cycle: all its
contributing tops lie in one two-dimensional face.  Hence a cross-gadget
cycle of length \(t\) uses at least \(\lceil t/4\rceil\) independent
positional words (and at least two); uncovered tops provide further
independent words.  Conditional on the first word,
each further word must induce one prescribed cyclic order, up to
rotation and reversal, on at least \(M-2r\) common labels.  Its
probability is at most

\[
                         \frac{\operatorname{poly}(M)^r}{(M-2r)!}.
\tag{4.1}
\]

The number of possible common cores is \(\exp(O(m))\), and for fixed
\(t\) the remaining label choices are polynomial; for growing \(t\)
they contribute at most \(\exp(O(t\log m))\).  Summing (4.1) with the
power \(\lceil t/4\rceil-1\) over \(3\le t\le2m\) tends to zero, since
\(\log((M-2r)!)=(1+o(1))M\log M\).  Thus with positive probability no
cross-gadget directed-cycle move exists.

For a cube not contained in one gadget, of dimension \(d\le R\), the number of
candidates is \(\exp(O(m))\), because \(d\) is fixed.  It uses at least
two independent words, and common-core compatibility again has
probability bounded by (4.1).  A union bound excludes all of them
simultaneously.  Fix one successful choice of words.  Equation (3.5) on
each gadget proves that the two global tables lie in the same exact
fibre, while the preceding exclusions make both isolated. \(\square\)

No asymptotic random construction is part of the claimed output: the
probabilistic argument proves existence of a deterministic catalogue.

### Corollary 4.2 (the MSW owner-star lift does not unlock the traps)

Every middle incidence in both isolated tables of Theorem 4.1 has a
literal MSW owner-star certificate.

#### Proof

At a selected top \(U=A^c\), every middle target of its frame has the
form \(D=A\cup J\), where \(J\) is an \(H\)-window.  Thus \(A\subset D\).
The exact owner-star theorem restricts the unique MSW row owning \(D\)
to \(U\) and supplies a literal frame witnessing that incidence.  This
applies independently to every selected incidence on both sides.
\(\square\)

The certificate need not be the selected frame in (3.4).  That is the
point: complete local witness availability does not imply a connected
global common-frame fibre.

## 5. Quantitative exceptional-frame consequence

There are

\[
                         \frac{N-o(N)}{2^{R+1}}
\tag{5.1}
\]

disjoint traps.  Deleting selected top rows cannot create an applicable
move.  To make the two endpoint tables agree outside an exceptional set,
or merely to hit every trap by a complete-frame replacement, therefore
requires at least (5.1) exceptional tops.  Since one top frame carries
\(M\) middle phase incidences, the exposed incidence mass is at least

\[
 \frac{M(N-o(N))}{2^{R+1}}
 =\left(2^{-(R+1)}-o(1)\right)W.
\tag{5.2}
\]

For fixed \(R\), this is not \(o(W)\).  If one demands the stronger
bound \(O(N)=O(W/M)\) on the phase-incidence replacement mass, then
(5.2) forces \(2^{R+1}=\Omega(M)\), which is (0.5).

This accounting is deliberately restricted to **complete-frame
replacement or deletion**.  If one arbitrary temporary frame can be
installed, used to enable many exchanges, removed, and recycled from
trap to trap, isolation of the endpoint monomials supplies no additive
lower bound.  Likewise, charging only an \(O(H)\) collar per exceptional
top gives \(HN/2^{R+1}=o(W)\) even for fixed \(R\), so (5.2) must not be
misquoted as a collar lower bound.

## 6. Implication for the \(O(N_H)\)-component braid

The common-core tight-path theorem needs one legal ordered path and one
nested tag history per top.  Once those columns exist with the required
all-depth injectivity, the delayed-atom compiler already uses only
\(N_H\) path blocks and pays \(O(HN_H)=o(W)\) collars.

The all-depth exchanges studied here do not obstruct that final
compilation.  Rather, they fail as a universal way of producing the
required columns:

* their load-neutrality requires the desired good load vector to be
  present before any move is applied;
* their legal columns always satisfy the nonabelian holonomy (1.6),
  while the separate clone-Hall projection does not enforce it; and
* every bounded placeholder-rank library has dense exact fibres on which
  its Markov graph is disconnected, even after all directed cycles are
  included.

Thus a positive braid must use at least one ingredient outside this
bounded-rank scheme: a growing-rank exchange, a non-coherent/catalytic
move which changes the intermediate load fibre, or a direct integral
construction of the CCTPF columns.  The moving-hole two-top transfer is
one genuinely nonneutral primitive, but its common-tag packing theorem
remains open.

## 7. Exact boundary

Proved:

1. the exact conjugacy-class lag-\(H\) holonomy;
2. invariance of all holes and floor energies under all audited
   load-neutral exchanges;
3. an \((R+1)\)-cube endpoint invisible to every internal directed-cycle
   move and every cube move of rank at most \(R\);
4. dense deterministic global isolation for every fixed \(R\);
5. compatibility of every isolated middle incidence with the exact MSW
   owner-star lift; and
6. the full-frame exceptional toll (5.2).

Not proved:

1. impossibility of a growing-rank exchange library;
2. impossibility of a recyclable catalytic frame;
3. an additive lower bound on final word components;
4. failure of the nonneutral moving-hole transfer; or
5. failure of CCTPF itself.

Accordingly this is a theorem-level obstruction to the proposed
bounded-rank exchange architecture, not a no-go for constant one.
