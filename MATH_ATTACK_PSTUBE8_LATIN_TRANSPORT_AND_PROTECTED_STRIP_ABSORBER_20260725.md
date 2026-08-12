# Two-update Latin transport, the PSTUBE8 chronology, and the protected-strip absorber test

Date: 2026-07-25

Method: pure mathematics only.  No computation, search, solver, or web input
is used.

## 0. Outcome

The local chronology part of \((\mathrm{PSTUBE}_8)\) has an exact positive
solution.  The complementary-triple endpoints of one four-carrier Latin
block can be changed into singleton-special sources for a fresh Latin block
in exactly two physical updates:

\[
 (d_1,p_i),\qquad(d_2,q_i)qquad(1\le i\le4).
 \tag{0.1}
\]

Here \(q_i\) is the old special label missing from carrier \(i\)'s endpoint
lower block, \(P=\{p_1,p_2,p_3,p_4\}\) is a fresh four-set in the common
residual intersection, and \(d_1,d_2\) are common lower departures.  The
first transport state has pairwise distinct middle owners; the second is the
next Latin source.  Transport is identical on both signs of the preceding
switch, so every connector flag cancels from the signed correction.

One Latin block uses two updates and its transport uses two.  A fixed
four-carrier tube therefore supplies

\[
 {M\over4}-O(1)
 \tag{0.2}
\]

rank-isolated bits.  Across \(N_H/4\) carrier quartets this is

\[
 {MN_H\over16}-o(W)
 =\left({1\over16}-o(1)\right)W,
 \tag{0.3}
\]

exactly the required correction scale.  The common residual reservoir is
conserved except when the transported adjacent swap straddles the
four-label ejection boundary.  This occurs only once per \(\Theta(Q)\)
cells and costs at most one common label, for aggregate loss \(O(M/Q)\) per
tube.  At central depth \(Q=\Theta(\sqrt m)\), the initial
\(H-Q-O(1)\) reservoir dominates this loss.

Compatible carrier quartets are also abundant enough: the hypergraph of
four \(M\)-sets sharing an \((M-1)\)-core has normalized codegrees
\(O(m^{-2})\) and a near-perfect matching.  Thus neither carrier grouping
nor finite connector chronology is the remaining obstruction.

This closes the finite-template triple-to-singleton obstruction.  It does
not by itself finish coefficient one.  For the owner-sensitive middle-cut
gadget, a signed cell has sixteen actual middle-owner occurrences, but the
union of its two signs has eighteen: the four connector owners are common to
both signs and are disjoint from the fourteen-owner robust Latin packet.
Thus sign-robust prepacking of these middle directions at density \(W/16\)
is impossible.  Their correction signs must be committed before the global
owner packing, or the transport itself must be made sign-dependent with a
new cancellation identity.

The eight-template family also does not black-box round the protected-strip
fractional multicover.  Every marked rectangle preserves total mass and all
coordinate marginals, and \(W/16\) rectangles can repair at most \(W/8\)
units of hole mass.  Since every missed protected-strip tag carries
\(K=\Theta(gQ)\) claims, this still requires a matching on a
\(1-O(1/Q)\) fraction of the tags.  The abstract protected-strip hypotheses
allow much larger matching leaves and do not force the marginal identities.
The Latin tube can be a terminal absorber only after a preliminary rounding
has produced a marginal-balanced defect of exchange distance at most
\((1/16-o(1))W\).

## 1. The exact quotient update

Write a quotient state as

\[
 \omega=(L;c_1,\ldots,c_n;R),
 \qquad n=2Q.
 \tag{1.1}
\]

One legal update with departure \(x\in L\) and arrival \(y\in R\) gives

\[
 \boxed{
 \begin{aligned}
 L'&=L-\{x\}+\{y\},\\
 (c'_1,\ldots,c'_n)&=(x,c_1,\ldots,c_{n-1}),\\
 R'&=R-\{y\}+\{c_n\}.
 \end{aligned}}
 \tag{1.2}
\]

Its middle owner is

\[
 F_Q(\omega)=L\cup\{c_1,\ldots,c_Q\}.
 \tag{1.3}
\]

Consequently the departure remains exposed at the front of the collar and
cancels from the owner update:

\[
 \boxed{F_Q(\omega')=F_Q(\omega)-\{c_Q\}+\{y\}.}
 \tag{1.4}
\]

This identity is the reason a common departure can change the physical
lower block without creating a common middle owner.

## 2. Endpoint normal form

Let \(S=\{s_1,s_2,s_3,s_4\}\), and let
\(q_1,q_2,q_3,q_4\) be a permutation of \(S\).  The four endpoints of a
Latin block have the form

\[
 \omega_i=
 \bigl(B+(S-\{q_i\});c_{i,1},\ldots,c_{i,n};R_i\bigr),
 \qquad1\le i\le4,
 \tag{2.1}
\]

where

\[
 q_i\in R_i.
 \tag{2.2}
\]

The lower core \(B\) and the collar label set are common.  Their collar
orders carry the allowed Latin base-chain braid (normally one prescribed
adjacent swap), and the residual blocks may differ.  Assume that their
common intersection contains a fresh set

\[
 P=\{p_1,p_2,p_3,p_4\}
 \subseteq\bigcap_iR_i,
 \qquad P\cap(S\cup B\cup\{c_{i,1},\ldots,c_{i,n}\})=\varnothing.
 \tag{2.3}
\]

Choose distinct common lower labels

\[
 d_1,d_2\in B.
 \tag{2.4}
\]

## 3. The two-update transport theorem

### Theorem 3.1 (triple-to-singleton Latin transport)

In carrier \(i\), apply the two updates

\[
 (d_1,p_i),\qquad(d_2,q_i).
 \tag{3.1}
\]

After the first update the state is

\[
 \omega_i^{(1)}=
 \bigl(B-d_1+(S-\{q_i\})+p_i;
       d_1,c_{i,1},\ldots,c_{i,n-1};
       R_i-p_i+c_{i,n}\bigr).
 \tag{3.2}
\]

After the second it is

\[
 \boxed{
 \omega_i^{(2)}=
 \bigl(A'+p_i;
       d_2,d_1,c_{i,1},\ldots,c_{i,n-2};
       R_i-\{p_i,q_i\}+\{c_{i,n-1},c_{i,n}\}\bigr),}
 \tag{3.3}
\]

where the new common lower core is

\[
 A'=B-\{d_1,d_2\}+S.
 \tag{3.4}
\]

Thus the four final states are singleton-special Latin sources relative to
the fresh special set \(P\): carrier \(i\) has \(p_i\) in its lower block
and \(P-\{p_i\}\) in its residual block.  The two common departures prepend
the same labels to every collar, while every pre-existing relative adjacent
swap is shifted two positions to the right.  Hence the allowed Latin collar
braid, rather than literal collar equality, is preserved for the next block.

#### Proof

Apply (1.2) twice.  The first update removes the common \(d_1\) and inserts
the carrier-specific \(p_i\).  The second removes the common \(d_2\) and
inserts the unique missing old special label \(q_i\).  Hence the old trace
\(S-\{q_i\}\) becomes all of \(S\), while the only carrier-dependent lower
label is \(p_i\).  Formula (3.3) follows.  Since every \(p_j\) initially
belongs to every \(R_i\) and only \(p_i\) is removed from \(R_i\), the final
residual contains \(P-\{p_i\}\). \(\square\)

The order in (3.1) matters.  If \(q_i\) is inserted first, all four lower
blocks and collars coalesce at the intermediate state and force three
duplicate owners per quartet.  Inserting \(p_i\) first preserves the
carrier identity until the next singleton source is reached.

### Proposition 3.2 (two updates are minimal)

No one-update transport can take (2.1) to singleton-special sources for a
fresh common-residual set \(P=\{p_1,p_2,p_3,p_4\}\) while preserving a
common lower core and the allowed collar braid.

#### Proof

A common prepended collar label forces the four departures to be the same
label \(d\).  To make carrier \(i\) the \(p_i\)-singleton fibre, its arrival must
be \(p_i\).  The four final lower blocks would then be

\[
 B-d+(S-\{q_i\})+p_i.
\]

Their common intersection is only \(B-d\), whereas four blocks of the form
\(A'+p_i\) have common intersection \(A'\), of size three larger.  Hence no
such common core \(A'\) exists. \(\square\)

## 4. Complete middle-owner separation

Put

\[
 X_i=F_Q(\omega_i),\qquad
 Y_i=F_Q(\omega_i^{(1)}),\qquad
 Z_i=F_Q(\omega_i^{(2)}).
\]

By (1.4), for \(Q\ge2\),

\[
 \boxed{
 Y_i=X_i-\{c_{i,Q}\}+\{p_i\},
 \qquad
 Z_i=Y_i-\{c_{i,Q-1}\}+\{q_i\}.}
 \tag{4.1}
\]

Relative to \((S,P)\), their signatures are

\[
\begin{array}{c|c}
\text{owner}&(|\cdot\cap S|,|\cdot\cap P|)\\ \hline
X_i&(3,0)\\
Y_i&(3,1)\\
Z_i&(4,1).
\end{array}
 \tag{4.2}
\]

### Proposition 4.1 (owner-simple transport)

All twelve owners

\[
 \{X_i,Y_i,Z_i:1\le i\le4\}
 \tag{4.3}
\]

are pairwise distinct.

#### Proof

Different rows of (4.2) cannot agree.  Within the first row, \(X_i\) omits
the distinct label \(q_i\).  Within the second, the ordered signature
\((q_i,p_i)\) is carrier-specific.  Within the third, \(Z_i\) contains the
carrier-specific \(p_i\). \(\square\)

Only the four \(Y_i\) are new state occurrences: the \(X_i\) are the old
block endpoints and the \(Z_i\) are the next block sources.  Thus one
transport uses exactly the one extra productive state per carrier available
in the coefficient ledger.

## 5. Signed incidence and indefinite repetition

The two arrival orders in one Latin diamond have the same endpoint inside
their carrier.  Therefore \(\omega_i\), and hence the entire transport
(3.1), is independent of the sign chosen in the preceding eight-template
switch.  The four transport paths occur identically on both sides.

### Proposition 5.1 (connector cancellation)

Adding the transport (3.1) after a Latin switch changes neither its complete
prefix-incidence difference nor its word-length difference.  In particular,
the switch remains zero at every rank except its marked rectangle.

#### Proof

The two signed configurations agree at \(\omega_i\) for every carrier and
then apply exactly the same updates.  Every transport state and every prefix
flag therefore occurs with the same multiplicity on both sides. \(\square\)

The transport can be repeated without depleting common arrivals at the
central-depth scale.  A complete
cell consists of two Latin updates followed by (3.1), hence four common
departures.  The four fresh labels in \(P\), initially in the common
residual intersection, are each removed from one carrier and therefore
leave that intersection.  At the same time, the four tail labels of each
collar enter its residual block by (1.2).  Their set is common unless the
transported adjacent swap straddles the boundary between the retained and
expelled four-label blocks; then the common intersection gains three labels
rather than four.

### Proposition 5.2 (common-reservoir conservation)

Away from a swap-boundary crossing, one complete four-update cell preserves
the size of the common residual intersection.  A crossing occurs at most
once per \(\Theta(Q)\) cells and loses at most one common label.  Hence a
length-\(M\) tube loses only \(O(M/Q)\) common labels.

The initial explicit quartet has common residual size \(H-Q-O(1)\).  Thus
central-depth repetition follows under

\[
 H-Q\gg M/Q,
\]

which holds for calibrated \(H\sim\sqrt{m\log m}\) and
\(Q=\Theta(\sqrt m)\).  Initial and terminal collar remainders cost
\(O(QN_H)=o(W)\).

## 6. Exact throughput and the remaining global packing problem

Carrier compatibility itself admits a clean near-factor.  Let
\(\mathcal Q_M\) be the four-uniform hypergraph whose vertices are the
\(M\)-subsets of \([2m]\), and whose edges are quartets

\[
 \{C+a_1,C+a_2,C+a_3,C+a_4\},
 \qquad |C|=M-1,
 \tag{6.0}
\]

with distinct \(a_i\notin C\).  Such a quartet has common intersection
\(C\), so it contains every common visible set of size at most \(M-1\) and
has a common residual reservoir of the required type.

### Proposition 6.1 (compatible carrier-quartet near-factor)

Every carrier tag has exact degree

\[
 \boxed{d_1^{\rm car}=M\binom{2m-M}{3}.}
 \tag{6.0a}
\]

Two distinct tags have codegree zero unless their intersection has size
\(M-1\); in that case their exact codegree is

\[
 \boxed{d_2^{\rm car}=\binom{2m-M-1}{2}.}
 \tag{6.0b}
\]

More generally, \(j\) distinct tags, \(2\le j\le4\), have nonzero
codegree only when their common intersection is one \((M-1)\)-set \(C\)
and they are distinct one-label extensions of \(C\).  Then the codegree is

\[
 \boxed{d_j^{\rm car}
 =\binom{2m-M+1-j}{4-j}.}
 \tag{6.0c}
\]

Consequently every normalized nontrivial codegree is \(O(m^{-2})\), and
\(\mathcal Q_M\) has a matching covering all but \(o(N_H)\) carrier tags.

#### Proof

For a fixed tag \(U\), choose the deleted label which gives
\(C=U-x\) in \(M\) ways, then choose the other three extensions from the
\(2m-M\) labels outside \(U\).  This proves (6.0a).  Two tags in one edge
must have common core equal to their \((M-1)\)-intersection; after fixing
their two extensions, choose the other two, proving (6.0b).  The same count
gives (6.0c).  Since \(M\asymp2m-M\asymp m\), the pair ratio is
\(O(m^2/m^4)=O(m^{-2})\), and higher ratios are smaller.  The audited
fixed-uniformity nibble therefore gives the near-perfect matching. \(\square\)

The visible Latin set has size \(m+Q+O(1)\), while
\(|C|=M-1=m+H-1\); since \(Q=o(H)\), it can be chosen inside the common
core of every matched quartet.

One useful Latin block and its transport use four updates on each of four
carriers and provide one independently signable marked rectangle.  A
four-carrier tube of length \(M\) therefore contains

\[
 \left\lfloor{M-O(Q)\over4}\right\rfloor
 ={M\over4}-o(M)
 \tag{6.1}
\]

directions.  If all but \(o(N_H)\) carriers are partitioned into compatible
quartets, the aggregate count is (0.3).

Each cell has four owner occurrences per carrier:

\[
 \text{source},\quad\text{Latin intermediate},\quad
 \text{endpoint},\quad\text{transport intermediate}.
 \tag{6.2}
\]

Proposition 4.1 and the twelve-owner Latin separation theorem show that all
sixteen are distinct inside either committed sign.  Thus a committed cell
has the exact coefficient ratio

\[
 16\text{ owners}:1\text{ direction}.
 \tag{6.3}
\]

This proves the local chronology and density assertions required by
\((\mathrm{PSTUBE}_8)\).  The remaining global theorem is a **tube
near-factor**, not another finite connector lemma: choose compatible carrier
quartets, their initial states, and their successive fresh special sets so
that the committed sixteen-owner cells over all tubes cover all but
\(o(W)\) middle owners.

Independent formal block matching does not prove this tube near-factor,
because the next source in (3.3) is constrained by the preceding endpoint.
The transport makes that constraint constant-length and reservoir-stable;
it does not erase it.

## 7. A sharp sign-robust obstruction

For one Latin block, either sign uses twelve owners while the union of both
signs uses fourteen.  The four transport-intermediate owners \(Y_i\) contain
fresh labels from \(P\), so they are outside that fourteen-owner union and
are common to both signs.  Therefore

\[
 \boxed{
 |\mathcal O^+_{\rm cell}|=|\mathcal O^-_{\rm cell}|=16,
 \qquad
 |\mathcal O^+_{\rm cell}\cup\mathcal O^-_{\rm cell}|=18.}
 \tag{7.1}
\]

At \((1/16-o(1))W\) cells, sign-robust owner reservation would require

\[
 {18W\over16}-o(W)=W+{W\over8}-o(W)
 \tag{7.2}
\]

distinct owners.  Hence:

### Theorem 7.1 (no sign-free full-cell prepacking)

No owner-disjoint packing of \((1/16-o(1))W\) transported Latin cells can
reserve both signs of every cell.  Any coefficient-one tube construction
must commit the correction signs before its final global owner packing, or
must use a sign-dependent transport whose extra incidence is itself an
exact coboundary.

This is a finite-template invariant, but it does not obstruct the committed
transport in Sections 3--6.

The qualification is important.  Equation (7.1) concerns the
owner-sensitive middle-cut perturb whose robust Latin packet has fourteen
owners.  If the isolated marked rank is outside the middle-owner-sensitive
indices, the adjacent chains have recoalesced at the middle observation and
the two signs can have the same twelve-owner support.  Then the transported
robust cell has sixteen, not eighteen, owners.  Such cells may be prepacked
sign-free at coefficient scale, but they correct nonmiddle protected flags;
they do not supply the missing middle-owner directions for which
\((\mathrm{PSTUBE}_8)\) was introduced.

## 8. Rectangle lattice seen by the absorber

At the marked middle rank, one gadget direction is

\[
 \rho=
 e_{K+v+a+b}+e_{K+u+a+c}
 -e_{K+v+a+c}-e_{K+u+a+b}.
 \tag{8.1}
\]

It satisfies

\[
 \boxed{
 \sum_X\rho_X=0,
 \qquad
 \sum_{X\ni j}\rho_X=0\quad(j\in[2m]).}
 \tag{8.2}
\]

Thus every sum of eight-template corrections preserves total mass and all
first coordinate marginals.

The same equations hold separately at every nonmiddle protected rank after
replacing \(m\) by that rank.  Hence defects cannot transfer total mass or
coordinate marginal error between protected rows by using rectangles at
other ranks.

Conversely, the integer lattice generated by all symmetric-exchange
rectangles in \(\binom{[2m]}m\) is exactly the kernel of the equations in
(8.2).  To see this, represent the positive and negative parts of an
integer kernel vector by two \(0\)-\(1\) matrices with row sum \(m\) and the
same column sums.  Their symmetric difference is a union of alternating
cycles.  Successive \(2\)-by-\(2\) switches shorten those cycles.

A switch between two rows \(A,B\), exchanging \(a\in A-B\) with
\(b\in B-A\), gives the symmetric-exchange relation

\[
 R(A,B;a,b)=e_A+e_B-e_{A-a+b}-e_{B-b+a}.
 \tag{8.2a}
\]

If \(|A-B|>2\), choose \(c\in A-B-\{a\}\) and
\(d\in B-A-\{b\}\), and put \(A_1=A-c+d\).  Then

\[
 R(A,B;a,b)=L+R(A_1,B;a,b),
 \tag{8.2b}
\]

where

\[
 L=e_A+e_{A-\{a,c\}+\{b,d\}}
   -e_{A-a+b}-e_{A-c+d}.
\]

The vector \(L\) is a local Johnson four-cycle of the form (8.1), while
\(|A_1-B|=|A-B|-1\); moreover \(a\in A_1-B\) and \(b\in B-A_1\).
Induction reduces every matrix switch to local Latin rectangles.  This
proves the asserted integer lattice equality.

This lattice equality is qualitative.  If

\[
 h(\delta)=\sum_X(\delta_X)_+
 ={1\over2}\|\delta\|_1,
 \tag{8.3}
\]

then one rectangle moves at most two positive units.  Hence any absorber
requires at least

\[
 {h(\delta)\over2}
 \tag{8.4}
\]

cells.  The matrix reduction uses at most \(O(mh(\delta))\) row switches,
and (8.2b) uses at most \(m\) local rectangles per row switch.  Thus the
audited general bound is only \(O(m^2h(\delta))\), so the marginal
identities and the scalar bound alone do not give a coefficient-safe
decomposition.

With only \(W/16\) cells, the necessary scalar capacity is

\[
 \boxed{h(\delta)\le {W\over8}+o(W).}
 \tag{8.5}
\]

## 9. Test against protected-strip fractional multicover coloring

The protected-strip fractional point has total mass \((1-o(1))T\), but its
abstract hypotheses do not provide an integral matching on the required
\(1-O(1/Q)\) fraction of the tags.  This already prevents the Latin family
from serving as a black-box absorber.

Indeed, omitting a fraction \(\varepsilon\) of the chunk tags loses
\((\varepsilon+o(1))W\) physical middle-owner mass.  Rectangles preserve
total mass, so they cannot create that missing mass.  Even if one first
balances holes against duplicates externally, (8.5) requires

\[
 \varepsilon\le{1\over8}+o(1).
 \tag{9.1}
\]

That middle-owner estimate is not the controlling protected-strip ledger.
Every missed chunk tag carries

\[
 K=\Theta(gQ)
\]

protected claims, while \(gT=(1+o(1))W\).  One rectangle repairs at most two
positive target units at one rank.  Therefore \(r\) missed tags require

\[
 Kr\le2\cdot{W\over16}+o(W)={W\over8}+o(W),
\]

and hence

\[
 \boxed{{r\over T}\le {g\over8K}+o(1/Q)=O(1/Q).}
 \tag{9.1a}
\]

Thus even a perfectly targeted Latin absorber does not remove the
\(1+O(1/Q)\) coloring/transversal accuracy requirement.  To leave only
\(o(W)\) unabsorbed protected claims one still needs \(r=o(T/Q)\), unless
essentially the entire \(W/16\) Latin reservoir is devoted to this one
purpose.

The projective-plane singleton-intersection construction gives the sharp
abstract warning.  In its parameter-matched form it has
\(N=k^2-k+1\) tags and \(R\) disjoint target planes; every matching contains
at most one edge from each plane, hence covers at most \(R\) tags.  Its
physical leave is \((1-R/N+o(1))W\), far above \(W/8\), despite exact
fractional tag and target capacities and zero nonlinear width-two moment.
At the corrected protected-strip scales,

\[
 K=m^{1+o(1)},\qquad \mu=m^{11/6-o(1)},\qquad
 {K^2\over\mu}=m^{1/6+o(1)},
\]

so taking \(k\asymp K\) and \(R\asymp\mu\) makes this abstract block
parameter-compatible; it is not known to embed in the actual rotor
catalogue.  Thus no proved catalogue-specific theorem currently gives the
needed \(1-O(1/Q)\)-transversal.  The width-two Shannon example separately shows why
coloring all rational copies can have a \(3/2\) gap; it is not being used
here as a bound on the maximum single matching.

There is a second obstruction.  A protected-strip integral choice can have
defect vector \(\delta\) with nonzero coordinate marginals

\[
 \sum_{X\ni j}\delta_X.
 \tag{9.2}
\]

Equation (8.2) shows that no collection of Latin rectangles changes these
marginals.  The fractional point is coordinate-symmetric in aggregate, but
the present coloring/rounding hypotheses do not transfer that symmetry to
one integral color class.

Therefore the eight-template packing does **not** replace either the
weighted rotor-transversal inequality or the catalogue-specific integral
resolution theorem.

It does give the following exact terminal-absorber statement.

> **Conditional protected-strip Latin absorber.**  Suppose a preliminary
> integral rounding commits a defect vector \(\delta\) such that:
> 1. its total and coordinate marginals vanish, up to an \(o(W)\) part to be
>    completed literally;
> 2. its symmetric-exchange distance is at most
>    \((1/16-o(1))W\); and
> 3. the required marked rectangles admit a compatible committed-sign Latin
>    tube near-factor.
>
> Then the two-update transports realize all those corrections with no
> additional interface toll, and the remaining literal completion is
> \(o(W)\).

The new work has therefore closed the finite transport gate but not the
protected-strip rounding gate.  The live global statement is the committed
tube near-factor in Section 6, coupled to a marginal-controlled
protected-strip matching theorem.
