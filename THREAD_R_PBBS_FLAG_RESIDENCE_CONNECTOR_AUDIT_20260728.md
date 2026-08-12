# PBBS flag-preserving connectors: exact seam ledgers, the MNW residence failure, and the true asymptotic boundary

Date: 2026-07-28

Method: pure mathematics and local-source audit only.  No web search,
finite search, certificate computation, or experimental inference is used.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W=\binom{2m+1}{m},\qquad
 B_m=\operatorname {Cat}_m=\frac{W}{2m+1}.
\tag{0.1}
\]

The audited conclusions are the following.

1. The canonical PBBS odd-graph factor already has the complete flag
   support needed at every depth.  For every
   \(1\le q\le m\) and every
   \(S\in\binom{[2m+1]}{m-q}\), it has a canonical oriented
   \(q\)-edge step-two path whose full intersection is \(S\), with
   occurrence load between

   \[
       1\quad\hbox{and}\quad \binom{2q+1}{q}.
   \tag{0.2}
   \]

2. The published GMN Hamiltonization theorem audited in
   MATH_AUDIT_PBBS_VERSUS_LEXICAL_MIDDLE_LEVELS_HAMILTONIZATION_20260726.md
   starts from the zero/one-lexical Middle Levels factor, not from PBBS.
   Already at \(m=2\), the PBBS lift has two components while the lexical
   factor has one.  Separately, the MNW joining flips audited below are
   alternating relative to the MSW minimum-cycle odd-graph seed; no theorem
   makes them PBBS-alternating.  Neither construction supplies a proved
   transport of the PBBS flag theorem.

3. Hamiltonizing the PBBS factor is not an asymptotic prerequisite for
   coefficient one.  The PBBS projected factor has at most \(B_m\)
   components.  Opening them and using the proved dominance-staircase
   collars costs at most \(2HB_m\) before the short-residence cuts.  At
   \(H=\lceil A\sqrt m\rceil\),

   \[
      \frac{2HB_m}{W}=\frac{2H}{2m+1}=O_A(m^{-1/2})=o_A(1).
   \tag{0.3}
   \]

   Thus component topology is already cheap.  By item 8 below, a
   Catalan-order local connector cannot even change the asymptotic
   short-residence regime.  Its remaining value is finite topology or an
   exact owner/seam implementation, not component joining by itself.

4. Every alternating odd-graph switch has an exact local flag ledger.  At
   edge-depth \(q\), only flags whose \(2q\)-edge span crosses a changed
   seam can change.  If the switch removes and inserts \(t\) edges, at most
   \(2qt\) old and \(2qt\) new flag occurrences are in the crossing
   ledgers.  There is an exact necessary-and-sufficient target-by-target
   inequality for preservation of complete support.

5. Every alternating odd-graph switch preserves the complete histogram of
   missing edge colours and the point degrees of the turn-colour
   multiset.  It can nevertheless change turn support and all higher flag
   supports.  Hence neither colour balance nor point-degree balance is a
   substitute for the flag ledger.

6. At depth three, under five-edge separation, residence survives a seam
   if and only if four distance-three and six distance-five inequalities
   hold.  More generally, the same theorem gives all odd-distance clauses
   through arbitrary depth \(d\).  It also gives the exact repair form:
   cut every inherited short return, then verify the new seam clauses.

7. The actual MSW/MNW base flip \(\beta\) is not residence-safe.  Its
   switched odd-graph word has exactly seven distance-three and three
   distance-five equalities.  Six of these defects are internal to its
   joining collars and survive as a single isolated MNW context embedding;
   in a compound schedule this conclusion requires those radius-five
   collars to remain untouched.
   Thus the published joining theorem cannot be supplemented by a blanket
   assertion that its flips preserve residence.

8. Suppose two projected cycle systems are obtained from the same retained
   path segments by deleting and reconnecting at at most \(J\) old and
   \(J\) new transition slots.  Then, for every \(H\),

   \[
       \left|\nu_H(F')-\nu_H(F)\right|\le J.
   \tag{0.4}
   \]

   This bound is independent of \(H\) and survives intervals crossing
   several seams and reversed segment orientations.  Consequently an
   \(O(B_m)\)-transition
   Hamiltonization changes \(\nu_H\) by only \(O(B_m)\).  At Gaussian
   depth this is \(o(B_m\sqrt m)\), so such a local Hamiltonization
   preserves whether the PBBS residence statistic is subcritical or
   critically saturated; it cannot manufacture the missing vanishing
   factor.

9. Rankwise marginal balancing is not a remaining obstruction.  The
   hypersimplex integer-decomposition theorem gives, whenever
   \(0\le\gamma_{q,x}\le e_q\), a hole-free rank-\((r-q)\) multiset with
   exactly the point degrees forced by the actual trace row.  In the frozen
   Hall-29 chronology the inequalities hold with large slack at
   \(q=2,3\).  What remains is the simultaneous lift of the chosen
   rankwise exchanges to one residence-safe chronology and one owner
   matching.

The remaining exact finite connector statement is therefore a decorated
physical splice theorem: realize enough PBBS residence-transversal cuts by
integral alternating switches, make every inserted collar safe, preserve
the required flag occurrences target by target, and extend the frozen owner
assignment through its exact residual Hall graph.  No cited theorem proves
that joint statement.  Separately, the asymptotic PBBS
dominance-staircase gate remains
\(\nu_{\lceil A\sqrt m\rceil}(P_m)=o_A(B_m\sqrt m)\), as isolated by
equation (24.7) of PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md.

## 1. Source separation and the all-depth PBBS input

Let \(f\) be the PBBS odd-graph permutation on
\(\binom{[n]}m\), and let \(g=f^2\) be its step-two projection.  On an
oriented odd-graph component write its vertices as

\[
             \ldots,A_j,A_{j+1},A_{j+2},\ldots .
\tag{1.1}
\]

For edge-depth \(q\ge0\), define the flag occurrence

\[
       \Phi_j^{[q]}(F):=\bigcap_{h=0}^{q}A_{j+2h}.
\tag{1.2}
\]

Thus \(q\) is the number of \(g\)-edges and the flag uses \(q+1\)
states.  The minimum, correct target rank is \(m-q\); ineffective or
repeated deletions can make an arbitrary occurrence larger.  The audited
load theorem below counts only correct-rank occurrences.

### Theorem 1.1 (audited PBBS all-depth flag support)

For every \(1\le q\le m\) and every
\(S\in\binom{[n]}{m-q}\), the PBBS factor has a canonically oriented
occurrence of (1.2) equal to \(S\).  If
\(\mu_{P,q}^{\rm corr}(S)\) counts the correct-rank canonical
occurrences, then

\[
       1\le \mu_{P,q}^{\rm corr}(S)
          \le \binom{2q+1}{q}.
\tag{1.3}
\]

This is Theorem 21.2 of
PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md, including the independently
audited global-maximum corridor.  The proof selects, among the
\(2q+1\) reverse-unmatched zeros of \(S\), the \(q\) deleted labels of
the starting state.  Those labels determine the oriented path, giving the
upper bound.  The two-sided maximum corridor constructs at least one such
path, giving the lower bound.

In the complement-antipodal setting of Theorem 2.6 of
MATH_K15_COMPLEMENT_ANTIPODAL_MIDDLE_LEVELS_REDUCTION_20260728.md, assume
that the Hamilton length \(W\) is odd, so multiplication by two permutes
the cyclic indices, and put \(B_i=A_{2i}\).  That theorem states

\[
 \begin{aligned}
 F_i^{(r)}
   &:=\bigcap_{h=0}^{r-1}B_{i+h}\\
   &=B_i\setminus
      \{z_{2i+1},z_{2i+3},\ldots,z_{2i+2r-3}\},
 \end{aligned}
\tag{1.4}
\]

where \(z_j\) is the missing colour of edge \(A_jA_{j+1}\).  In the
notation (1.2), \(F_i^{(q+1)}=\Phi_{2i}^{[q]}\).  The lifted chronology is
upper-universal at every rank exactly when these flags cover every target
layer.  Thus turn coverage is only the row \(q=1\), not a separate design
problem.

The support statement (1.3) is integral and occurrence-level.  It is not a
claim that every PBBS window has correct rank, nor is its exponential
pointwise upper bound an aggregate collision estimate.

### Proposition 1.2 (the audited GMN lexical theorem does not transfer)

The audited GMN short Hamiltonization theorem applies to the union of the
zero- and one-lexical matchings.  It does not apply to the PBBS lift.
Indeed, for \(m=2\), the PBBS odd-graph orbits are

\[
 (12,34,15,23,45),\qquad(13,24,35,14,25),
\tag{1.5}
\]

so the bipartite lift has two ten-cycles.  The lexical factor has one
component, since there is one plane tree with two edges, hence it is one
twenty-cycle.  Component number is invariant under coordinate relabeling
and shore exchange.  Therefore these two \(m=2\) instances are not
conjugate, and the cited lexical theorem is not a uniform
coordinate-conjugate PBBS theorem.  This does not rule out a new
scale-specific transfer construction.

This is the decisive source boundary: lexical flippability and PBBS flag
support do not combine automatically; a new transfer theorem would be
required.

## 2. Component topology is already asymptotically cheap

Let \(c_2(P_m)\) be the number of complement-projected step-two PBBS
cycles.  The exact PBBS reduction gives

\[
                         c_2(P_m)\le B_m.
\tag{2.1}
\]

For \(2H\le m+1\), the linear dominance-staircase construction gives the
central-band ledger

\[
 L_H\le W+2HB_m+2(5H-1)\nu_H(P_m).
\tag{2.2}
\]

Here \(2HB_m\) is the entire component/cyclic-collar term.  The last term
is the residence-transversal term.

### Theorem 2.1 (Hamiltonization is not the asymptotic gate)

Fix \(A>0\), and put \(H_A=\lceil A\sqrt m\rceil\).  For all sufficiently
large \(m\), the PBBS cycles may be left unmerged, and their total topology
cost in (2.2) is

\[
       2H_AB_m=O_A(W/\sqrt m)=o_A(W).
\tag{2.3}
\]

Consequently a theorem which merely reduces \(c_2(P_m)\) to one cannot
settle coefficient one in the PBBS dominance-staircase route.  More
precisely, conditional for every fixed \(A>0\) on

\[
       \nu_{H_A}(P_m)=o_A(B_m\sqrt m),
\tag{2.4}
\]

coefficient one already follows from (2.2) without any Hamiltonization.

#### Proof

Equation (2.1) permits one cyclic collar of length at most \(2H_A\) for
each component.  Since \(W=(2m+1)B_m\),

\[
       \frac{2H_AB_m}{W}=\frac{2H_A}{2m+1}
           =O_A(m^{-1/2}).
\]

The condition \(2H_A\le m+1\) holds for fixed \(A\) and all sufficiently
large \(m\).  This proves (2.3).  The remaining term in (2.2) depends on
\(\nu_H\), not on component count.  \(\square\)

For the asymptotic literal word, the dominance-staircase theorem supplies
the seam charts at this cost.  For an exact finite one-factor or wreath
formula, a seam letter must additionally fit the frozen palette and owner
assignment.  That is an integral Hall extension problem and is not implied
by (2.3).  This is why topology can be asymptotically harmless while seam
ownership remains decisive for the exact finite formula.

The proof of the staircase ledger is local to components.  Hence, for any
other projected factor \(F\) which retains the same complete correct flag
tower and admits the same literal seam charts, its generic form is

\[
 L_H(F)\le W+2Hc_2(F)+2(5H-1)\nu_H(F).
\tag{2.5}
\]

This conditional generic ledger is the correct formula to use after a
connector switch.  One must not replace \(\nu_H(P_m)\) in (2.2) by a new
factor's statistic without first proving preservation of its flag tower and
physical seam/owner realization.

## 3. Two invariants of every alternating odd-graph switch

Let \(F\) be a simple two-factor of \(O_m=KG(n,m)\), let \(Z\) be an
\(F\)-alternating cycle of length \(2t\), and put

\[
 E_-=E(Z)\cap E(F),\qquad E_+=E(Z)\setminus E(F),
 \qquad F'=F\mathbin\triangle Z.
\tag{3.1}
\]

For an odd-graph edge \(XY\), let

\[
             \chi(XY)=\text{the unique element of }
                       [n]\setminus(X\cup Y).
\tag{3.2}
\]

### Lemma 3.1 (alternating shores have the same colour histogram)

For every \(x\in[n]\),

\[
 \#\{e\in E_-:\chi(e)=x\}
 =\#\{e\in E_+:\chi(e)=x\}.
\tag{3.3}
\]

#### Proof

Write the alternating cycle as
\(X_0X_1\cdots X_{2t-1}X_0\), and put
\(u_i={\mathbf 1}_{x\in X_i}\).  Since adjacent odd-graph vertices are
disjoint, \(u_iu_{i+1}=0\), and therefore

\[
 {\mathbf 1}_{\chi(X_iX_{i+1})=x}=1-u_i-u_{i+1}.
\]

The alternating sum of the right side is zero:

\[
 \sum_i(-1)^i(1-u_i-u_{i+1})
 =0-\sum_i(-1)^iu_i+\sum_i(-1)^iu_i=0.
\]

Its even and odd edge counts are therefore equal.  \(\square\)

Thus a switch can only reorder occurrences of each omitted colour.  It
cannot change their global supply.

At a vertex \(X\), if its two incident factor-edge colours are \(c_-,c_+\),
the turn set is

\[
             \operatorname {Turn}_F(X)
             =X^c\setminus\{c_-,c_+\}.
\tag{3.4}
\]

At a port of the switch, let \(r_X\) be the retained incident colour,
\(a_X\) the removed colour, and \(b_X\) the inserted colour.

### Lemma 3.2 (turn one-swap law and point-degree invariance)

At every port,

\[
 \begin{aligned}
 \operatorname {Turn}_F(X)&=X^c\setminus\{r_X,a_X\},\\
 \operatorname {Turn}_{F'}(X)&=X^c\setminus\{r_X,b_X\}\\
  &=\bigl(\operatorname {Turn}_F(X)\setminus\{b_X\}\bigr)
       \cup\{a_X\}.
 \end{aligned}
\tag{3.5}
\]

All nonport turns are unchanged.  Moreover, for every coordinate \(x\),
the number of turn sets containing \(x\) is the same in \(F\) and
\(F'\).

#### Proof

Formula (3.5) follows from (3.4); the three incident edges are distinct, so
their colours are pairwise distinct.  Summing the signed incidence changes
over the ports gives

\[
  \sum_X(e_{a_X}-e_{b_X})
   =2\left(\sum_{e\in E_-}e_{\chi(e)}
            -\sum_{e\in E_+}e_{\chi(e)}\right)=0
\]

by Lemma 3.1.  \(\square\)

Point-degree invariance is a genuine obstruction to any proposed switch
whose claimed turn repair changes point marginals.  It does not preserve
the turn multiset or its support.

## 4. Exact residence seam theorem at every finite depth

Give each component of \(F'\) an orientation after the switch.  Delete
\(E_-\); every retained path is then traversed in either its old direction
or its reverse.  At an inserted edge of colour \(b\), write the local word

\[
 \ldots,L_s,\ldots,L_2,L_1,b,R_1,R_2,\ldots,R_s,\ldots .
\tag{4.1}
\]

### Theorem 4.1 (general odd-distance seam criterion)

Fix \(d\ge1\).  Assume that every retained path between two consecutive
inserted edges in \(F'\) has at least \(2d-1\) edges.  Then every
distance-\(s\) equality in \(F'\), for odd
\(1\le s\le2d-1\), is of exactly one of the following two kinds.

1. It lies wholly in one retained path and is an inherited equality from
   \(F\), possibly read in reverse.
2. It crosses one inserted edge, and at that seam it is one of

   \[
      b=L_s,\qquad b=R_s,\qquad
      L_u=R_{s-u}\quad(1\le u\le s-1).
   \tag{4.2}
   \]

Consequently, if \(F\) is depth-\(d\) resident, then \(F'\) is
depth-\(d\) resident if and only if every equality in (4.2) is absent at
every seam.  More generally, if the removed edges meet every inherited bad
interval through distance \(2d-1\), the same seam inequalities are
necessary and sufficient for \(F'\) to be depth-\(d\) resident.

#### Proof

An interval of at most \(2d-1\) edge positions contains at most one
inserted edge by the separation hypothesis.  With no inserted edge, it is
inside one retained path, proving case 1.  If the inserted edge is the
right endpoint, the compared pair is \((L_s,b)\); if it is the left
endpoint, the pair is \((b,R_s)\).  If it is internal, it has exactly
\(u\) positions to the left and \(s-u\) to the right for one
\(1\le u<s\), giving \((L_u,R_{s-u})\).  These cases are exhaustive and
each listed equality is itself a bad return.  Cutting an inherited interval
removes it; an uncut inherited interval remains.  \(\square\)

The distance-one clauses \(b\ne L_1,R_1\) are automatic in a simple
two-factor, since a fixed odd-graph vertex has a unique neighbour for each
missing colour.

For \(d=3\), the nonautomatic criterion consists of exactly ten clauses:

\[
\boxed{
\begin{array}{rclcrcl}
b&\ne&L_3,&&b&\ne&R_3,\\
L_1&\ne&R_2,&&L_2&\ne&R_1,\\[1mm]
b&\ne&L_5,&&b&\ne&R_5,\\
L_1&\ne&R_4,&&L_2&\ne&R_3,\\
L_3&\ne&R_2,&&L_4&\ne&R_1.
\end{array}}
\tag{4.3}
\]

The first four are exactly distance three and the last six exactly distance
five.  If five-edge separation fails, the correct test is not the product
of independent seam tests: one must inspect every distance-three/five pair
whose interval meets the union of the changed seam collars.

Theorem 4.1 is the precise form of a residence-improving connector: its
removed edges must hit the old bad intervals, while its inserted collars
must avoid (4.2).  Mere component merging supplies neither condition.

## 5. Exact all-depth flag seam ledger

For a two-factor \(F\), let \({\cal M}_q(F)\) be the multiset of all flag
occurrences (1.2), over all starts in one chosen orientation of each
component.  Both directions are not counted separately.  Reversing one
chosen component orientation does not change this multiset: a reversed flag
is the same intersection read from its other endpoint.

For the switch (3.1), let \({\cal X}_{q}^{-}\) be the multiset of old
flags whose directed \(2q\)-edge span meets \(E_-\), and let
\({\cal X}_{q}^{+}\) be the analogous multiset of new flags whose span
meets \(E_+\).

### Theorem 5.1 (exact flag cancellation away from seams)

\[
 \boxed{
       {\cal M}_q(F')-{\cal M}_q(F)
       ={\cal X}_{q}^{+}-{\cal X}_{q}^{-}.}
\tag{5.1}
\]

If \(|E_-|=|E_+|=t\), then

\[
       |{\cal X}_{q}^{-}|\le2qt,qquad
       |{\cal X}_{q}^{+}|\le2qt.
\tag{5.2}
\]

#### Proof

An old flag on an untouched component cancels identically.  On a component
met by the switch, a span avoiding \(E_-\) lies in one retained path.  In
the new factor that path is traversed in the same direction or in reverse.
In the first case the same start gives the same intersection; in the
second, the other endpoint gives the same intersection with the factors
reordered.
This is a bijection between old and new flags whose spans avoid the changed
edges.  They cancel in the signed multiset, proving (5.1).

If a cycle has length greater than \(2q\), a fixed edge lies in exactly
\(2q\) directed spans of length \(2q\).  If its length is at most
\(2q\), it has at most \(2q\) starts in total.  Thus in every case a
fixed edge is met by at most \(2q\) flag starts.  Taking a union bound over
the \(t\) changed edges proves (5.2).  \(\square\)

For a target set \(S\), write \(x_{q,S}^{\pm}\) for its multiplicity in
\({\cal X}_{q}^{\pm}\).  Equation (5.1) gives the exact scalar identity

\[
 \mu_{F',q}(S)
  =\mu_{F,q}(S)-x_{q,S}^{-}+x_{q,S}^{+}.
\tag{5.3}
\]

### Corollary 5.2 (necessary and sufficient support condition)

Suppose \(F\) covers every target in
\(\binom{[n]}{m-q}\).  Then \(F'\) covers every such target if and only
if

\[
 \boxed{
    x_{q,S}^{-}-x_{q,S}^{+}
       \le \mu_{F,q}(S)-1
    \quad\hbox{for every }S\in\binom{[n]}{m-q}.}
\tag{5.4}
\]

In particular, equality

\[
                 {\cal X}_{q}^{+}={\cal X}_{q}^{-}
\tag{5.5}
\]

is a sufficient flag-neutrality condition.  A weaker sufficient condition
is to select one canonical PBBS witness for every target and forbid the
removed seams from meeting any selected witness span.

For the PBBS seed, (1.3) is the only general multiplicity information.
Because the lower bound is exactly one, the upper bound
\(\binom{2q+1}{q}\) gives no redundancy for a target whose selected or
only occurrence crosses a seam.  Aggregate edit counts alone therefore do
not imply support preservation.

At \(q=1\), Theorem 5.1 is the turn-colour ledger of Lemma 3.2.  For a
switch with \(t\) changed edges, the six port turns of a \(C_6\), for
example, are precisely the seam-crossing first flags.  For larger \(q\),
the theorem is the required all-depth replacement for a generic turn bound.

Summing (5.2) over \(1\le q\le H\) gives the conservative occurrence bound

\[
 \sum_{q=1}^{H}
 (|{\cal X}_{q}^{-}|+|{\cal X}_{q}^{+}|)
 \le 2tH(H+1).
\tag{5.6}
\]

This is not a word-length lower bound.  The nested dominance-staircase chart
compresses a full seam tower to \(O(H)\) literal letters; equation (5.6)
only records how many raw flag occurrences can change.

### Theorem 5.3 (rankwise marginal completion is already solved)

Let \(T=(T_0,\ldots,T_{W-1})\) be a depth-\(d\) resident Hamilton path in
\(J(k,r)\), and put

\[
 L_i^{(q)}=\bigcap_{h=0}^{q}T_{i+h},\qquad
 e_q=W-q-\binom{k}{r-q}.
\tag{5.7}
\]

Let \(\gamma_{q,x}\) be the forced excess-degree vector from the exact
cross-depth transport law.  If

\[
                 0\le\gamma_{q,x}\le e_q
                 \qquad(x\in[k]),
\tag{5.8}
\]

then there is a hole-free multiset \(M_q^*\) of exactly \(W-q\)
rank-\((r-q)\) blocks having the same point-degree vector as the actual
trace row \((L_i^{(q)})\).  Moreover the actual row and \(M_q^*\) are
connected by integral symmetric two-block exchanges.

#### Proof

The transport and scalar ledgers give

\[
                 \sum_x\gamma_{q,x}=(r-q)e_q.
\tag{5.9}
\]

The integer-decomposition property of the hypersimplex decomposes
\(\gamma_q\) into the incidence vectors of exactly \(e_q\)
rank-\((r-q)\) sets.  Adjoin these excess blocks to one copy of every
rank-\((r-q)\) target.  The result has \(W-q\) blocks, no holes, and the
required degrees.  Two uniform multisets with the same block count and
point degrees differ by alternating cycles in their incidence bipartite
graphs; decomposing those cycles gives symmetric \(2\times2\) block
exchanges.  This is Theorem 2.1 of
MATH_HYPERSIMPLEX_MARGINAL_COMPLETION_AND_CHRONOLOGY_GATE_20260728.md.
\(\square\)

For the frozen Hall-29 data at \((k,r,W)=(15,8,6435)\),

\[
\begin{array}{c|c|c}
q&e_q&\{\gamma_{q,x}:x\in[15]\}\\ \hline
2&1428&\text{all values lie in }[568,574],\\
3&3429&\text{all values lie in }[1138,1147].
\end{array}
\tag{5.10}
\]

Thus the observed \(q=2,3\) holes are not forced by total multiplicity,
point degrees, or the complete rankwise exchange lattice.  Lemma 3.2
remains a valid switch invariant, but it is not a no-go: degree-matched
hole-free rows exist.

The exact unresolved object is a simultaneous hypersimplex lift.  One must
choose the rankwise two-block exchanges so that they are all induced by one
deletion/insertion chronology, equivalently one common family of nested
flags, while preserving residence, upper occurrences, and the owner
matching.  Conditions (5.4) and (8.2) are occurrence-level parts of that
simultaneous lift; proving another independent rankwise balancing lemma
would not advance it.

## 6. Exact edit stability of the short-residence transversal

Let \({\cal I}_H(F)\) be the PBBS return intervals arising from two
consecutive occurrences of one omitted edge colour at odd gap
\(2s+1\), with \(s+1\le H\).  Let \(\nu_H(F)\) be their maximum
step-two-transition-edge-disjoint packing number.

Consecutive occurrences of a fixed missing colour in an oriented
odd-graph cycle have odd gap.  Indeed, after an edge of colour \(x\), the
recurrence
\[
 A_{j+2}=A_j-\{z_{j+1}\}+\{z_j\}
\]
inserts \(x\) into one parity of vertices; the next colour-\(x\) edge is
exactly the transition which deletes it from that parity.  Thus the
return-interval definition remains valid after an odd-graph switch.

### Theorem 6.1 (transition-edit stability, independent of \(H\))

Let \(F_-\) and \(F_+\) be two cyclic transition systems obtained by
cutting and reconnecting the same collection of retained path segments.
The retained segments may be reversed.  Let \(D_-\) be the deleted old
transition slots and \(D_+\) the inserted new transition slots, and assume

\[
                     |D_-|,|D_+|\le J.
\tag{6.1}
\]

Then, for every \(H\),

\[
\boxed{
       |\nu_H(F_+)-\nu_H(F_-)|\le J.}
\tag{6.2}
\]

#### Proof

Let \({\cal U}\) be the interval hypergraph consisting of residence
intervals whose entire step-two transition-edge set, including both
boundary transitions in the residence convention, is wholly contained in
one retained segment interior.  Reversing a segment reverses such an
interval but preserves its physical transition-edge set, so the same
\({\cal U}\) is a subhypergraph of both old and new interval systems.

Every old interval outside \({\cal U}\) crosses at least one transition in
\(D_-\), including an interval crossing the old cyclic boundary.  In an
edge-disjoint packing, at most one packed interval can contain a specified
transition.  Even if one interval crosses several seams, choose any one of
its seam transitions; two packed intervals cannot choose the same
transition because they are edge-disjoint.  Hence a packing contains at
most \(|D_-|\) old intervals outside \({\cal U}\).  The identical argument
on the new side gives at most \(|D_+|\) new intervals outside
\({\cal U}\).  Therefore

\[
\nu_H({\cal U})\le\nu_H(F_-)\le\nu_H({\cal U})+|D_-|,
\]
\[
\nu_H({\cal U})\le\nu_H(F_+)\le\nu_H({\cal U})+|D_+|.
\tag{6.3}
\]

Both packing numbers lie in the same interval of length \(J\), proving
(6.2).  This proof explicitly includes multi-seam intervals, cyclic
boundaries, and reversed segments.  \(\square\)

### Corollary 6.2 (odd-graph switches)
If an alternating odd-graph switch removes and inserts \(t\) odd-graph
edges, then it changes at most \(2t\) projected step-two transition slots,
and consequently

\[
                  |\nu_H(F')-\nu_H(F)|\le2t.
\tag{6.4}
\]

For a sequence with \(T\) total changed odd-graph seam edges,
\[
                  |\nu_H(F_s)-\nu_H(F_0)|\le2T.
\tag{6.5}
\]

#### Proof

The projected transition from \(A_j\) to \(A_{j+2}\) uses the two-edge
odd-graph arc \(A_jA_{j+1}A_{j+2}\).  A fixed changed odd edge lies in at
most the two projected transitions starting immediately before it and at
it.  Thus the old and new projected seam sets each have size at most
\(2t\).  Apply Theorem 6.1 and then telescope.  \(\square\)

In particular, an odd-graph \(C_6\) switch has \(t=3\) and changes
\(\nu_H\) by at most six, for every \(H\).

### Corollary 6.3 (Catalan-edit rigidity at Gaussian depth)

Let \(H_A=\lceil A\sqrt m\rceil\) for fixed \(A>0\).  If a local
rethreading or Hamiltonization changes \(J_m=O_A(B_m)\) projected
transition slots, then

\[
 |\nu_{H_A}(F_m)-\nu_{H_A}(P_m)|=O_A(B_m)
       =o_A(B_m\sqrt m).
\tag{6.6}
\]

Hence

\[
\boxed{
\nu_{H_A}(F_m)=o_A(B_m\sqrt m)
\quad\Longleftrightarrow\quad
\nu_{H_A}(P_m)=o_A(B_m\sqrt m).}
\tag{6.7}
\]

An \(O(B_m)\)-edit connector therefore preserves the subcritical-versus-
critical residence regime.  It cannot convert reciprocal-height
saturation with a positive \(B_m\sqrt m\)-scale limsup into the vanishing
estimate required by the dominance-staircase route.  Conversely it cannot
destroy that estimate if PBBS already has it.  This is stronger than an
\(O(HB_m)\) seam-count bound and changes the strategic conclusion:
Hamiltonization can serve topology or finite owner compatibility, but
local Catalan-order edits cannot create the missing asymptotic residence
improvement.

## 7. Adversarial audit of the actual MSW/MNW \(\beta\)-flip

This section concerns the MSW minimum-cycle odd-graph factor and the MNW
joining move.  It is not asserted to be a PBBS connector or a GMN lexical
flip.

For \(m=3\), lift a rank-three word \(x\) on \([6]\) to
\(\operatorname {supp}(x)\), and a rank-four word \(y\) to

\[
       ([6]\setminus\operatorname {supp}(y))\cup\{\infty\}.
\tag{7.1}
\]

The MNW base cycle

\[
 (111000,111001,011001,011011,011010,111010)
\tag{7.2}
\]

becomes the odd-graph alternating cycle

\[
 (123,45\infty,236,14\infty,235,46\infty).
\tag{7.3}
\]

The old shore colours are \((6,5,1)\), and the new shore colours are
\((1,6,5)\), as required by Lemma 3.1.  The three old cycle words are

\[
\begin{aligned}
q_A&=(6,2,4,3,5,1,\infty),\\
q_B&=(2,1,6,4,5,3,\infty),\\
q_C&=(2,1,4,3,6,5,\infty).
\end{aligned}
\tag{7.4}
\]

Respecting the reversal of the third retained strand, the switched
twenty-one-cycle has colour word, up to rotation and reversal,

\[
\boxed{
q'=(5,2,\infty,5,6,3,4,6,3,\infty,2,1,6,4,
     1,2,4,3,5,1,\infty).}
\tag{7.5}
\]

Indexing from zero, its complete list of distance-three equalities is

\[
 (0,3):5,\ (4,7):6,\ (5,8):3,\ (11,14):1,
 \ (13,16):4,\ (18,0):5,\ (20,2):\infty,
\tag{7.6}
\]

and its complete list of distance-five equalities is

\[
              (7,12):6,\qquad(10,15):2,
              \qquad(14,19):1.
\tag{7.7}
\]

There is no adjacent equality.  An independent substitution into (4.3)
reproduces exactly the seven plus three defects, so they are not an
orientation artifact.

The six port turns change as follows:

\[
\begin{array}{c|c|c|c|c}
X&r_X&a_X\to b_X&\text{old turn}&\text{new turn}\\ \hline
123&\infty&6\to5&45&46\\
45\infty&2&6\to1&13&36\\
236&4&5\to1&1\infty&5\infty\\
14\infty&3&5\to6&26&25\\
235&4&1\to6&6\infty&1\infty\\
46\infty&2&1\to5&35&13.
\end{array}
\tag{7.8}
\]

After cancelling the two relocated turn values, the signed turn-multiset
change is

\[
 e_{46}+e_{36}+e_{5\infty}+e_{25}
 -e_{45}-e_{26}-e_{6\infty}-e_{35}.
\tag{7.9}
\]

Its point degrees cancel, in agreement with Lemma 3.2, but its support
does not remain fixed.

The MNW context operations act on internal missing colours by injective
relabelings: suffix appending leaves the old labels fixed, prefixing by a
Dyck word of length \(L\) sends \(c\mapsto L+c\), and mirror wrapping
sends \(c\mapsto N+2-c\), possibly reversing cyclic order.  Therefore
equality and odd distance are preserved for patterns lying wholly inside a
retained local block.  The \(\beta\) collar contains the six such defects

\[
\begin{array}{c|c}
\text{new seam }6&6_{-3}=6_0,\quad3_{-2}=3_{+1},\\
\text{new seam }1&1_{-3}=1_0,\quad4_{-1}=4_{+2},
 \quad2_{-4}=2_{+1},\quad1_0=1_{+5}.
\end{array}
\tag{7.10}
\]

The first four equalities have distance three and the last two displayed
at seam \(1\) have distance five.  Hence a single MNW context copy of
\(\beta\), or a compound schedule in which no other switch changes an edge
in these radius-five collars and the displayed strand orientations are
retained, is residence-unsafe.  Physical vertex-disjointness of switching
cycles alone does not imply this collar condition.  Later switches which
meet these collars could repair the defects, so this is not a no-go theorem
for a fully correlated final schedule.

The published MNW joining theorem proves alternation, compatibility of its
selected flips, and Hamiltonicity for the MSW odd-graph seed.  It does not
state the seam inequalities (4.3), preservation of turn support, or
all-depth flag support.

## 8. The exact conditional PBBS splice theorem

The preceding ledgers combine into a useful theorem, but its hypotheses
are not currently supplied by a PBBS connector construction.

### Theorem 8.1 (residence-safe, flag-safe integral splice)

Let \(F_0=P_m\) be the PBBS factor.  Perform a finite sequence of integral
alternating odd-graph switches, producing \(F_s\).  Fix integers
\(1\le d,H\le m\).  Assume the following.

1. At every stage \(F_{j-1}\to F_j\), every bad odd-colour interval of
   \(F_{j-1}\) through distance \(2d-1\) meets the removed shore
   \(E_{-,j}\).  In particular, the first removed shore is a transversal
   of all initial PBBS bad intervals in this range.  This is an
   intentionally strong simultaneous/per-stage hypothesis, not a gradual
   cumulative-repair assumption.
2. At every insertion stage, either the seams have the separation of
   Theorem 4.1 and satisfy all its clauses through distance \(2d-1\), or
   the complete overlapping seam-collar union has been checked directly
   and certified to contain no bad equality in this range.
3. For every \(1\le q\le H\) and every
   \(S\in\binom{[n]}{m-q}\), the cumulative crossing ledger satisfies

   \[
    \sum_{j=1}^{s}
       \bigl(x_{j,q,S}^{-}-x_{j,q,S}^{+}\bigr)
       \le \mu_{P,q}^{\rm corr}(S)-1.
   \tag{8.1}
   \]

   Here \(x_{j,q,S}^{-}\) and \(x_{j,q,S}^{+}\) are the full crossing
   multiplicities for the current stage \(F_{j-1}\to F_j\), not just the
   initially designated PBBS witnesses.

Then \(F_s\) is depth-\(d\) resident and retains complete PBBS flag
support through edge-depth \(H\).  If the switches also make one component,
then \(F_s\) is a resident Hamilton cycle with that flag support.

#### Proof

Apply Theorem 4.1 at the first stage.  Hypothesis 1 eliminates every
inherited bad interval and hypothesis 2 eliminates every new seam equality,
so \(F_1\) is depth-\(d\) resident.  Inductively the same two hypotheses
make every \(F_j\) depth-\(d\) resident.
Telescoping (5.3) over the switches gives

\[
 \begin{aligned}
 \mu_{F_s,q}(S)
 &=\mu_{P_m,q}(S)
  -\sum_jx_{j,q,S}^{-}+\sum_jx_{j,q,S}^{+}\\
 &\ge \mu_{P,q}^{\rm corr}(S)
  -\sum_jx_{j,q,S}^{-}+\sum_jx_{j,q,S}^{+}.
 \end{aligned}
\]

Hypothesis 3 makes this at least one for every target.  Component merging
is independent of these two conclusions.  \(\square\)

For a frozen exact owner assignment, add the following genuinely separate
condition.  First fix the chronology and every bundled seam choice, so that
the remaining freedom is an ordinary one-token/one-slot assignment.  Let
\({\cal D}\) be the target-depth tokens on all shores simultaneously whose
designated old owner slots were removed, let \({\cal P}\) be the available
unit-capacity new seam or palette slots after all unaffected owners are
frozen, and join \(D\in{\cal D}\) to
\(p\in{\cal P}\) exactly when the literal set at \(p\) has the required
target and satisfies every owner/containment rule.  In this fixed
bipartite residual problem, the owner extension exists if and only if

\[
          |N_\Gamma({\cal U})|\ge|{\cal U}|
          \quad\text{for every }{\cal U}\subseteq{\cal D}.
\tag{8.2}
\]

This is Hall's theorem applied after the background is frozen.  Neither
flag support (8.1) nor the asymptotic collar estimate (2.3) proves (8.2).
Thus an exact finite connector certificate must include its all-shore
residual Hall certificate; palette cardinality alone is insufficient.  If
the seam choices themselves couple several slots, those choices must be
resolved before (8.2), or retained as a stronger bundled matching problem;
plain Hall inequalities on the unexpanded tokens would then not suffice.

Theorem 5.3 removes point marginals from this Hall obstruction.  In
particular, at Hall-29 depths two and three, a residual failure must come
from the inability to realize the rankwise hypersimplex decompositions by
one nested chronology and one common owner assignment.  It cannot be
certified from either depth row's marginal vector alone.

Theorem 8.1 is intentionally stronger than what coefficient one needs.
By Theorem 2.1, the asymptotic construction may leave the PBBS cycles open.
If a switched factor satisfies the flag and owner hypotheses needed for
the generic ledger (2.5), Corollary 6.3 shows that an \(O(B_m)\)-transition
connector has the same subcritical-versus-critical residence status as
PBBS.  Such a connector may still be useful for the exact finite owner
extension, but it cannot create the vanishing Gaussian residence factor
missing from PBBS.

## 9. What the existing PBBS connector atlas does not yet prove

The separate PBBS connector theorem
MATH_THEOREM_PBBS_HAMILTONIZATION_CONNECTOR_BOUNDARY_20260726.md proves a
large integral atlas of fixed-\(M_0\), \(M_1\)-switching alternating
\(C_6\)'s in the bipartite Middle Levels lift, including an asymptotic
\((2/3)B_m\) vertex-disjoint reservoir, and isolates an unproved
component-quotient loose-tree statement.  Under that statement the
hexagons directly Hamiltonize the Middle Levels lift.  They do not by
themselves form a simple odd-graph two-factor switch: after
upper-complement projection, the unchanged shore copy remains.  A
paired-shore or direct projected-path seam compiler is therefore required
before applying the odd-graph residence and flag theorems of Sections 4--6.

The atlas theorem does not provide any of the following decorated facts.

1. A residence transversal whose cut edges are the old shores of a
   dynamically compatible switch family.
2. A compiled odd-graph/projected seam chronology whose determined collars
   have been audited against (4.2).  The existing Middle Levels
   matching-slot collars alone do not supply this.
3. The target-by-target all-depth inequalities (5.4).
4. The residual owner Hall inequalities (8.2).
5. A simultaneous hypersimplex lift realizing the desired rankwise
   two-block exchanges in one nested deletion chronology.

Even if the loose-tree statement were proved and its matching-slot switches
were compiled into an odd-graph/path-seam realization with \(O(B_m)\)
changed transition slots, Theorem 6.1 would give
\[
             |\Delta\nu_H|=O(B_m)
\tag{9.1}
\]
independently of \(H\).  Hence it would preserve the ST_A status by
Corollary 6.3, not repair a critical PBBS plateau.  The loose-tree theorem
does not supply the paired-shore compiler or the residence/flag/owner
decoration.  In either formulation, topology alone does not close the
asymptotic gate.

Conversely, failure of the MSW/MNW \(\beta\)-flip does not obstruct the
PBBS atlas.  It proves only that residence is not a formal consequence of
alternation, edge-disjointness, context embedding, or component merging.
The PBBS collars must be computed in their own edge-colour chronology.

## 10. Sharp proved/conditional boundary

### Proved

1. PBBS has complete canonical flag support at every depth with (0.2).
2. The \(m=2\) component count refutes a uniform identification of the
   PBBS lift with the GMN lexical factor; the published lexical theorem
   supplies no automatic PBBS transfer.
3. Leaving all PBBS components open costs only \(O(HB_m)=o(W)\) at fixed
   Gaussian height in the PBBS dominance-staircase architecture.
   Hamiltonicity is not the gate in that route.
4. Alternating switches preserve missing-colour histograms and turn point
   degrees.
5. The residence seam criterion (4.2), its exact depth-three specialization
   (4.3), and the all-depth flag identity (5.1) are necessary and sufficient
   in their stated scopes.
6. The residence packing obeys the \(H\)-independent transition-edit
   stability bound (6.2); an odd-graph \(t\)-edge switch changes it by at
   most \(2t\).
7. The MSW/MNW \(\beta\)-flip destroys distance-three and distance-five
   residence; six defects persist for a single context copy, and under a
   compound schedule only while its radius-five collars remain untouched.
8. Under the hypersimplex bounds, every depth row has a hole-free
   degree-matched multiset in its integral rankwise exchange class.  For
   Hall-29 the bounds hold at \(q=2,3\) with the exact ranges (5.10).
9. An \(O(B_m)\)-transition connector cannot alter the ST_A truth value.
   Any change at the critical \(B_m\sqrt m\) scale requires more than
   Catalan-order local transition edits, or an operation outside the
   retained-segment splice model.

### Conditional only

1. Theorem 8.1 gives a correct PBBS Hamiltonization-and-preservation theorem
   if one constructs the decorated switches satisfying its hypotheses.
2. A topology-only PBBS loose tree remains useful for a finite Hamilton
   formula, but it must be supplemented by (4.2), (5.4), and (8.2).
3. The rankwise hole-free completions are not known to lift simultaneously
   to one PBBS/Johnson chronology or to the frozen owner system.

### Sharp remaining obstructions, separated by scope

For the asymptotic PBBS dominance-staircase architecture, the sharp
remaining input is

\[
 \nu_{\lceil A\sqrt m\rceil}(P_m)=o_A(B_m\sqrt m)
 \qquad\text{for every fixed }A>0.
\tag{10.1}
\]

By Corollary 6.3, a Catalan-order local Hamiltonization neither proves nor
changes (10.1).  Component connectivity is therefore not an alternative
route around this residence gate.

For an exact finite decorated PBBS connector, no current theorem constructs
a dynamically compatible integral switch family which simultaneously

\[
\begin{array}{l}
\text{hits a sufficiently small short-residence transversal,}\quad
\text{has safe inserted collars,}\\
\text{realizes one simultaneous hypersimplex lift,}\\
\text{preserves the needed canonical flag witnesses, and}\\
\text{satisfies the frozen exact owner Hall system.}
\end{array}
\tag{10.2}
\]

These are different statements: (10.2) matters to a finite
Hamilton/one-factor formula, while (10.1) is already sufficient
asymptotically without Hamiltonizing.  No claim of coefficient one, PBBS
Hamiltonization, simultaneous hypersimplex lift, or automatic owner
extension is made.
