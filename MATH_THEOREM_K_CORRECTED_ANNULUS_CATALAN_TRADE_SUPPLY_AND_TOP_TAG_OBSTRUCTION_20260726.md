# Corrected Gaussian annulus: Catalan-trade supply, hereditary action, and the top-tag obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, web input,
or entropy heuristic is used.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 q_0=\lceil a\sqrt m\rceil,\qquad
 H=\lfloor b\sqrt m\rfloor,
\tag{0.1}
\]

where \(0<a<b\) are fixed, and write

\[
 N_q=\binom{2m}{m-q},\qquad
 R=m-q_0,\qquad D=H-q_0.
\tag{0.2}
\]

The corrected annulus needs only

\[
 N_{q_0}=(e^{-a^2}+o(1))W
\tag{0.3}
\]

paid middle-owner occurrences.  An ordinary cyclic packet has \(n=2m\)
starts, so the required packet count is

\[
 K_0=\left\lfloor{N_{q_0}\over2m}\right\rfloor.
\tag{0.4}
\]

This changes the Catalan supply calculation sharply.  Since

\[
 \operatorname{Cat}_m={W\over m+1},
\tag{0.5}
\]

one packet per Dyck root requires asymptotic root density

\[
 \boxed{
 {K_0\over\operatorname{Cat}_m}
 ={e^{-a^2}\over2}+o(1).}
\tag{0.6}
\]

Thus Catalan scale is no longer automatically too small.  A bank of
root density \(\theta\), supplying at most \(p\) ordinary packets per
active root, is numerically impossible when

\[
 \boxed{p\theta<{e^{-a^2}\over2}.}
\tag{0.7}
\]

Above (0.7), cardinality alone gives no obstruction.  Three exact gates
remain.

1. **Provider/transversal supply.**  The complete candidate bank must
   contain all but \(o(W)\) of the entrance and deeper target providers,
   and enough distinct middle-owner providers.  Exact inequalities are
   given in Section 2.
2. **Hereditary chronology.**  The oriented rank-\(q_0\) trace cycle
   reconstructs the whole packet.  All deeper colours are its consecutive
   path intersections.  A trade preserving that oriented trace has zero
   annular action.  A trade changing \(r\) entrance-trace positions changes
   at most \(r(D+1)(D+2)\) signed target occurrences over the whole
   annulus.
3. **SCD/Dyck top-tag chronology.**  In the SCD scaffold, if

   \[
      b^2-a^2<\log2,
   \tag{0.8}
   \]

   then every coefficient-one path/cycle realization needs

   \[
      \bigl(2e^{-b^2}-e^{-a^2}-o(1)\bigr)W
   \tag{0.9}
   \]

   genuine top-tag rotor arcs.  Averaged over the \(K_0\) ordinary
   \(2m\)-cycles, a fraction at least

   \[
      \boxed{
      \gamma_{a,b}:=2e^{-(b^2-a^2)}-1-o(1)>0}
   \tag{0.10}
   \]

   of all cycle arcs must be top--top arcs.  Consequently, when the
   unmodified scaffold has only \(o(W)\) available top--top arcs, a
   positive density of bounded-fringe Catalan trades, each supplying
   \(o(m)\) such arcs, cannot realize the SCD annulus.  Root-scale
   \(\Theta(m)\) chronological action per selected root is necessary.

The last theorem is an actual statewise obstruction on the SCD/Dyck
route, not an entropy claim.  It does not rule out an unrelated coloured
cyclic-order partial factor.  For arbitrary ordinary packets, the sharp
surviving object is precisely the coloured annulus partial-factor programme
of Section 6.

## 1. Ordinary cyclic packets and the corrected supply threshold

Let \(\pi=(\pi_0,\ldots,\pi_{n-1})\) be a directed cyclic ordering of
\([n]\).  For \(1\le s<n\), put

\[
 I_\pi(j,s)=\{\pi_j,\pi_{j+1},\ldots,\pi_{j+s-1}\},
 \qquad j\in\mathbb Z_n.
\tag{1.1}
\]

At annulus entrance, one packet supplies the \(n\) distinct targets

\[
 E_R(\pi)=\{I_\pi(j,R):j\in\mathbb Z_n\}.
\tag{1.2}
\]

At the middle rank it supplies the \(n\) cyclic \(m\)-interval owners.
The cyclic ordering is strongly safe through every depth less than \(m\).

### Theorem 1.1 (packet-count lower bound)

Let \(\mathcal F\) be any family of ordinary cyclic packets whose
rank-\(R\) hole count is \(h_R\).  Then

\[
 \boxed{
 |\mathcal F|\ge {N_{q_0}-h_R\over2m}.}
\tag{1.3}
\]

In particular, \(h_R=o(W)\) forces

\[
 |\mathcal F|\ge K_0-o(W/m).
\tag{1.4}
\]

#### Proof

The family has \(2m|\mathcal F|\) entrance occurrences and therefore
covers at most that many distinct entrance targets.  It must cover
\(N_{q_0}-h_R\) targets.  This proves (1.3).  Since
\(h_R/(2m)=o(W/m)\), (1.4) follows. \(\square\)

### Corollary 1.2 (Catalan-density threshold)

Suppose a trade bank contains at most

\[
 T_m=(\theta+o(1))\operatorname{Cat}_m
\tag{1.5}
\]

active Dyck roots, and every active root can contribute at most \(p\)
ordinary packets to one final family.  If the entrance holes are \(o(W)\),
then

\[
 \boxed{p\theta\ge{e^{-a^2}\over2}.}
\tag{1.6}
\]

#### Proof

Theorem 1.1 gives \(pT_m\ge K_0-o(W/m)\).  Divide by
\(\operatorname{Cat}_m=W/(m+1)\), and use

\[
 {N_{q_0}\over W}=e^{-a^2}+o(1).
\]

This gives (1.6). \(\square\)

The theorem counts complete packets, not switches.  A phase-complete
root trade can act on \(\Theta(m)\) owner occurrences and may supply one
packet.  A bounded physical switch acting on \(O(1)\) owners does not.
These two notions must not be assigned the same Catalan count.

## 2. Exact provider-union and owner-transversal obstruction

Let \(\mathscr C\) be any catalogue of candidate packets.  For
\(0\le d\le D\), define its lower provider union

\[
 \mathcal U_d(\mathscr C)
 =\bigcup_{\pi\in\mathscr C}E_{R-d}(\pi),
\tag{2.1}
\]

and its middle-owner union

\[
 \mathcal U_m(\mathscr C)
 =\bigcup_{\pi\in\mathscr C}E_m(\pi).
\tag{2.2}
\]

Complementation supplies the upper provider union from the lower one.

### Theorem 2.1 (catalogue deficiencies)

Every selected subfamily \(\mathcal F\subseteq\mathscr C\) of size
\(K_0\) obeys

\[
 \boxed{
 C_0(\mathcal F)\ge
  \bigl(2mK_0-|\mathcal U_m(\mathscr C)|\bigr)_+,}
\tag{2.3}
\]

and, for every \(0\le d\le D\),

\[
 \boxed{
 H_{q_0+d}(\mathcal F)\ge
 N_{q_0+d}-|\mathcal U_d(\mathscr C)|.}
\tag{2.4}
\]

Consequently the weak annulus gate is impossible whenever

\[
 \boxed{
 \bigl(2mK_0-|\mathcal U_m(\mathscr C)|\bigr)_+
 +\sum_{d=0}^{D}
   \bigl(N_{q_0+d}-|\mathcal U_d(\mathscr C)|\bigr)
 \ne o(W).}
\tag{2.5}
\]

#### Proof

The selected packets have \(2mK_0\) middle-owner occurrences.  Their
distinct owner support is contained in \(\mathcal U_m(\mathscr C)\), so
the collision excess is at least (2.3).  Every selected depth-
\((q_0+d)\) target lies in \(\mathcal U_d(\mathscr C)\), proving (2.4).
Sum. \(\square\)

Equation (2.5) is only the catalogue-union cut.  Even equality up to
\(o(W)\) does not select one common subfamily.  The remaining grouped
transversal problem is the integral programme in Section 6.

## 3. Hereditary trace rigidity

For a packet \(\pi\), orient its entrance trace as

\[
 T_j=I_\pi(j,R),\qquad j\in\mathbb Z_n.
\tag{3.1}
\]

Then

\[
 T_{j+1}=T_j-\{\pi_j\}+\{\pi_{j+R}\}.
\tag{3.2}
\]

### Theorem 3.1 (reconstruction and heredity)

The oriented cyclic list \((T_j)_{j\in\mathbb Z_n}\) determines the
cyclic order \(\pi\).  Moreover, for every \(0\le d\le D\),

\[
 \boxed{
 I_\pi(j+d,R-d)=\bigcap_{k=0}^{d}T_{j+k}.}
\tag{3.3}
\]

The complementary upper interval is given exactly by

\[
 [n]\setminus I_\pi(j,R-d)
 =I_\pi(j+R-d,n-R+d).                                  \tag{3.4}
\]

Hence the oriented entrance trace determines both signs at every depth
through \(H\).

#### Proof

Equation (3.2) gives

\[
 \{\pi_j\}=T_j\setminus T_{j+1}.
\tag{3.5}
\]

Thus all symbols of \(\pi\), with their cyclic positions, are recovered.
For (3.3), the intervals \([j+k,j+k+R-1]\), \(0\le k\le d\), have
intersection \([j+d,j+R-1]\), which has length \(R-d\).  This proves
the lower identity.  The positions not in the cyclic interval from \(j\)
through \(j+R-d-1\) are precisely those from \(j+R-d\) through \(j-1\),
proving (3.4) and the upper statement. \(\square\)

### Corollary 3.2 (no hidden Dyck decoration)

Any Catalan/Dyck trade which preserves the oriented entrance trace cycle
preserves every target occurrence at every depth \(q_0\le q\le H\), on
both signs.  It has zero annular action.

Thus a rank-\(q_0\) near-factor cannot first be selected and then repaired
at deeper ranks by changing an internal Dyck, product, pair-frame, or SCD
decoration.  The cyclic order itself is the remaining variable.

## 4. Exact local-action bound

Let \(\pi,\pi'\) be two phase-aligned candidate packets and put

\[
 r(\pi,\pi')
 =|\{j:T_j(\pi)\ne T_j(\pi')\}|.
\tag{4.1}
\]

For one sign, let \(A_d(\pi,\pi')\) be the number of starts at which the
depth-\((q_0+d)\) target occurrences differ.

### Theorem 4.1 (hereditary action Lipschitz bound)

For \(0\le d\le D\),

\[
 \boxed{A_d(\pi,\pi')\le(d+1)r(\pi,\pi').}
\tag{4.2}
\]

Over both signs and the whole annulus,

\[
 \boxed{
 A_{[q_0,H]}(\pi,\pi')
 \le r(\pi,\pi')(D+1)(D+2).}
\tag{4.3}
\]

#### Proof

By (3.3), a lower depth-
\((q_0+d)\) occurrence can differ only if one of its \(d+1\) entrance
trace vertices differs.  The cyclic union bound gives (4.2).  The upper
ledger is an antipodal complement of the lower ledger and has the same
bound.  Therefore

\[
 A_{[q_0,H]}
 \le2r\sum_{d=0}^{D}(d+1)
 =r(D+1)(D+2).
\]

This proves (4.3). \(\square\)

Changing one target occurrence can reduce the corresponding hole count
by at most one.  Thus for a sequence of packet trades
\(\mathcal F_0,\ldots,\mathcal F_t\), with phase-aligned entrance action
\(r_i\) at step \(i\),

\[
 \boxed{
 \mathcal H_{[q_0,H]}(\mathcal F_t)
 \ge
 \mathcal H_{[q_0,H]}(\mathcal F_0)
 -(D+1)(D+2)\sum_{i=1}^{t}r_i.}
\tag{4.4}
\]

This is a conditional no-go with an explicit premise, not an assertion
that every starting family has a large defect.  If

\[
 \mathcal H_{[q_0,H]}(\mathcal F_0)
 \ge\eta W(D+1)
\tag{4.5}
\]

for fixed \(\eta>0\), and the final defect is \(o(W)\), then

\[
 \boxed{
 \sum_{i=1}^{t}r_i
 \ge(\eta-o(1)){W\over D+2}.}
\tag{4.6}
\]

At \(D=\Theta(\sqrt m)\), a bank of \(\Theta(\operatorname{Cat}_m)\)
trades must therefore change \(\Omega(\sqrt m)\) entrance-trace positions
per trade on average whenever (4.5) holds.  Bounded-fringe trades cannot
repair such a baseline.  This statement applies, for example, only after
a separate theorem establishes (4.5) for the proposed baseline; it is not
an entropy-based universal impossibility claim.

There is an analogous exact owner-collision bound.  If a trade changes
\(u_i\) middle-owner occurrences, it can lower \(C_0\) by at most \(u_i\).
Therefore a baseline with \(C_0\ge\zeta W\) requires
\(\sum_i u_i\ge(\zeta-o(1))W\).  A Catalan-size bank then needs
\(\Omega(m)\) middle-owner action per trade on average.

### Theorem 4.2 (exact two-boundary ceiling for local word trades)

Let \(1\le s<n\).  One adjacent transposition at cyclic positions
\(t,t+1\) changes exactly the two *indexed* length-\(s\) interval
occurrences with starts

\[
                     t-s+1\quad\hbox{and}\quad t+1
                     \pmod n.                       \tag{4.7}
\]

Consequently the symmetric difference of the two unlabelled target
families has size at most four.  More generally, if an arbitrary
permutation is supported on one cyclic block of \(\ell\) positions and

\[
                         \ell\le s,\qquad\ell\le n-s, \tag{4.8}
\]

then at most

\[
                            2(\ell-1)                \tag{4.9}
\]

indexed length-\(s\) occurrences change.

#### Proof

A window is unchanged as a set if it contains both transposed positions
or neither.  Since the positions are adjacent, precisely one window ends
at \(t\) and precisely one begins at \(t+1\); these are (4.7).

For the block statement, a window is unchanged if it contains the whole
support block or is disjoint from it.  A possibly changed window must cut
one of the two block boundaries.  Under (4.8), the two boundary bands are
disjoint, and each contains exactly \(\ell-1\) starts.  This proves
(4.9). \(\square\)

Suppose candidate packet \(i\) is obtained from a baseline packet by
\(v_i\) adjacent transpositions.  At every annular depth the number of
new lower occurrences is at most \(2v_i\), and the same is true for the
upper ledger.  Hence the total possible reduction of the two-signed hole
count over all \(D+1\) depths is at most

\[
                 \boxed{4(D+1)\sum_i v_i.}           \tag{4.10}
\]

The possible reduction of middle-owner collision excess is at most
\(2\sum_i v_i\).  Thus a Catalan-size local-rewrite bank with

\[
             \sum_i v_i=o\!\left({W\over D+1}\right) \tag{4.11}
\]

has only \(o(W)\) total weak-gate action.  If it acts on
\(\Theta(\operatorname{Cat}_m)=\Theta(W/m)\) rows, this says that average
adjacent-swap width

\[
                         o\!\left({m\over D+1}\right) \tag{4.12}
\]

is insufficient to repair a separately established \(\Omega(W)\)
defect.  For \(D=\Theta(\sqrt m)\), the threshold is
\(o(\sqrt m)\) swaps per active row.  The same conclusion holds for
block rewrites after replacing \(v_i\) by \(\ell_i-1\).

There is a useful exact calibration for the fixed-slot reciprocal-
\(C_8\) bank.  For one prescribed four-position slot, and for two
prescribed disjoint slots, the respective active-root proportions are

\[
 p_1={2\operatorname{Cat}_{m-2}\over\operatorname{Cat}_m}
 ={m(m+1)\over2(2m-1)(2m-3)}\longrightarrow{1\over8},
\tag{4.13}
\]

\[
 p_2={4\operatorname{Cat}_{m-4}\over\operatorname{Cat}_m}
 ={(m+1)m(m-1)(m-2)\over
 4(2m-1)(2m-3)(2m-5)(2m-7)}
 \longrightarrow{1\over64}.                         \tag{4.14}
\]

Each layer has \(2\operatorname{Cat}_{m-2}\) active rows and contributes
two adjacent transpositions on each active row.  Therefore, for \(u\)
disjoint fixed-slot layers, overlaps included with their literal
multiplicity,

\[
                  \boxed{\sum_x d(x)=
                  4u\operatorname{Cat}_{m-2}.}       \tag{4.15}
\]

This is the unweighted edit action, not the component-weighted overlay
moment.  In particular fixed \(u\) gives only \(O(W/m)\) edits and hence
only \(O(W(D+1)/m)=o(W)\) annular action when
\(D=\Theta(\sqrt m)\).

## 5. The SCD/Dyck top-tag obstruction

Fix a symmetric chain decomposition \(\mathcal D\) of \(B_{2m}\).  Retain
its chains of tag at least \(q_0\), and choose radius-\(H\) extensions.
There are exactly \(N_{q_0}\) retained states, and their designated flags
cover every lower and upper annular target.  Suppose these states are put
in a radius-\(H\) rotor path cover with \(p=o(W/H)\) paths.

Let \(\lambda_H(\mathcal D)\) be the maximum number of genuine rotor arcs
in a vertex-disjoint directed linear forest induced by the tag-\(H\)
states.  The audited top-tag run theorem gives

\[
 \lambda_H(\mathcal D)
 \ge2N_H-N_{q_0}-p.
\tag{5.1}
\]

### Theorem 5.1 (linear top-tag action, including the used-arc form)

For a path cover as above, let \(e_{HH}\) denote the number of selected
arcs whose two endpoint states both have tag \(H\).  Then

\[
 \boxed{e_{HH}\ge2N_H-N_{q_0}-p,}
 \qquad e_{HH}\le\lambda_H(\mathcal D).
\tag{5.2}
\]

If \(b^2-a^2<\log2\), every such coefficient-one SCD/Dyck chronology
therefore obeys

\[
 \boxed{
 \lambda_H(\mathcal D)
 \ge
 \bigl(2e^{-b^2}-e^{-a^2}-o(1)\bigr)W.}
\tag{5.3}
\]

If instead all but

\[
 \rho=N_{q_0}-2mK_0<2m
\tag{5.4}
\]

states are put into \(K_0\) ordinary length-\(2m\) rotor cycles, and
\(e_{HH}^{\circ}\) is the number of top--top arcs actually used by those
cycles, then the sharper cyclic-word count gives

\[
 \boxed{e_{HH}^{\circ}\ge2N_H-N_{q_0}-\rho.}
\tag{5.5}
\]

Deleting one top--top arc from each all-top cyclic component, when
necessary, gives the inherited linear-forest consequence

\[
 \lambda_H(\mathcal D)
 \ge2N_H-N_{q_0}-\rho-K_0.
\tag{5.6}
\]

#### Proof

For paths, read each path as a word in \(\{\mathsf H,\mathsf O\}\).
The number of nonempty \(\mathsf H\)-runs is at most the number of
\(\mathsf O\)-vertices plus one per path.  Hence

\[
 e_{HH}\ge N_H-(N_{q_0}-N_H+p)
 =2N_H-N_{q_0}-p.
\]

Top-tag bridge rigidity makes every such selected arc a genuine rotor
arc, and the selected arcs form a linear forest, proving (5.2).
Equation (5.3) follows from (5.2) and

\[
 {N_{q_0}\over W}=e^{-a^2+o(1)},\qquad
 {N_H\over W}=e^{-b^2+o(1)}.
\]

For cycles, let \(M_H\) and \(M_O\) be the used numbers of top and
non-top states.  In a directed cyclic \(\mathsf H/\mathsf O\)-word, the
number of \(\mathsf H\!\to\!\mathsf O\) transitions is at most the
number of \(\mathsf O\)-vertices (with zero transitions on an all-top
cycle).  Therefore

\[
 e_{HH}^{\circ}
 =M_H-e_{HO}
 \ge M_H-M_O=2M_H-(N_{q_0}-\rho).
\]

At most \(\rho\) omitted states are top states, so
\(M_H\ge N_H-\rho\), proving (5.5).  Removing at most one arc from each
of the \(K_0\) cycles turns the selected top--top arcs into a directed
linear forest and proves (5.6).  Finally
\(\rho+K_0=o(W)\), so both the actual used-arc and linear-forest versions
have the same positive asymptotic coefficient. \(\square\)

### Corollary 5.2 (positive top-tag fraction in every average packet)

Let

\[
 \gamma_{a,b}=2e^{-(b^2-a^2)}-1>0.
\tag{5.7}
\]

In the cycle setting of Theorem 5.1, the mean number of required
top--top rotor arcs actually used per selected cycle is at least

\[
 \boxed{2m\gamma_{a,b}-o(m).}
\tag{5.8}
\]

The exact finite-
\(m\) arc fraction and per-cycle bounds underlying this assertion are

\[
 \boxed{
 {e_{HH}^{\circ}\over 2mK_0}
 \ge {2N_H-N_{q_0}-\rho\over N_{q_0}-\rho},
 \qquad
 {e_{HH}^{\circ}\over K_0}
 \ge {2N_H-N_{q_0}-\rho\over K_0}.}
\tag{5.9}
\]

#### Proof

Divide the used-arc bound (5.5) by

\[
 K_0=(e^{-a^2}+o(1)){W\over2m}.
\]

The quotient is

\[
 2m\bigl(2e^{a^2-b^2}-1-o(1)\bigr),
\]

which is (5.8); division of (5.5) by
\(2mK_0=N_{q_0}-\rho\) and by \(K_0\) gives (5.9). \(\square\)

### Corollary 5.3 (bounded Catalan trades fail on the SCD route)

Suppose the unmodified common SCD scaffold initially makes a set
\(B_0\) of genuine top--top rotor arcs available, with
\(\kappa_0=|B_0|\).  Suppose also that a trade bank has at most

\[
 (\theta+o(1))\operatorname{Cat}_m
\]

active trades, and trade \(i\) can add at most \(\kappa_i\) genuine
tag-\(H\)-to-tag-\(H\) rotor arcs to the available retained-state graph.
Under (0.8), a necessary condition is

\[
 \boxed{
 \kappa_0+\sum_i\kappa_i
 \ge
 \bigl(2e^{-b^2}-e^{-a^2}-o(1)\bigr)W.}
\tag{5.10}
\]

In particular, if \(\kappa_0=o(W)\) and
\(\kappa_i\le\kappa_m\) for every trade, then the exact carrier-width
ceiling is

\[
 \boxed{
 \kappa_m\ge
 {\bigl(2N_H-N_{q_0}-\rho-\kappa_0\bigr)_+\over T_m},}
 \qquad
 T_m:=|\text{trade bank}|,
\tag{5.11}
\]

and, for fixed \(\theta>0\) with
\(T_m\le(\theta+o(1))\operatorname{Cat}_m\), this becomes

\[
 \boxed{
 \kappa_m
 \ge
 {2e^{-b^2}-e^{-a^2}\over\theta}(m+1)-o(m).}
\tag{5.12}
\]

Every bounded-fringe library with \(\kappa_m=o(m)\), including every
bounded-support perturbation of an SCD whose original tag-\(H\) rotor
graph is empty, is therefore impossible on this route.

#### Proof

Every top--top arc used by the final cycles must belong to
\(B_0\) or to the union of the arcs added by the trades.  Hence the
cardinality of the available union is at most
\(\kappa_0+\sum_i\kappa_i\).  The actual used-arc bound (5.5), rather
than merely the ambient maximum-forest bound, gives (5.10).  If there are
at most \(T_m\) trades and each adds at most \(\kappa_m\) arcs, the same
inequality rearranges to (5.11).  Use
\(\operatorname{Cat}_m=W/(m+1)\) to obtain (5.12). \(\square\)

This corollary assumes a common SCD scaffold and counts actual new rotor
arcs, not formal trade options or relabelled profiles.  A construction
mixing provider states from unrelated SCDs lies outside its scope.

## 6. Sharp surviving criterion

For an ordinary packet \(\pi\), put

\[
 a_{d,T}(\pi)
 =\mathbf1_{\{T\in E_{R-d}(\pi)\}},
 \qquad0\le d\le D,
\tag{6.1}
\]

and let \(b_X(\pi)\) indicate that \(X\) is one of its middle owners.
The exact weak integral criterion is to choose

\[
 x_\pi\in\{0,1\},\qquad
 \sum_\pi x_\pi=K_0,
\tag{6.2}
\]

so that

\[
 \boxed{
 2mK_0-\sum_X\min\left\{1,\sum_\pi b_X(\pi)x_\pi\right\}
 +2\sum_{d=0}^{D}\sum_T
   \left(1-\sum_\pi a_{d,T}(\pi)x_\pi\right)_+
 =o(W).}
\tag{6.3}
\]

The factor \(2\) uses complement symmetry.  Equation (6.3) is exactly
middle collision excess plus the two signed annular hole count.  It is
the coloured annulus partial-factor gate, restricted to whatever
Catalan/Dyck packet catalogue is actually legal.

The uniform complete-cyclic-order fractional point has middle load
\(e^{-a^2}+o(1)<1\), covers every deeper target to load at least one,
and has only the unavoidable floor deficit
\(N_{q_0}-2mK_0=\rho<2m\) in aggregate at the entrance.  Thus there is
no asymptotic fractional capacity obstruction in the complete catalogue.
For a
restricted Catalan trade bank, Theorem 2.1 is its first exact statewise
test.  If that test passes, neither density nor local codegrees decide
(6.3): the cyclic grouping and all consecutive path colours remain.

## 7. Proved and conditional boundary

The following is proved.

1. The exact required packet count is
   \(K_0=(e^{-a^2}+o(1))W/(2m)\).
2. A one-packet-per-root Catalan bank needs density at least
   \(e^{-a^2}/2\).
3. Catalogue provider-union deficiencies (2.3)--(2.5) are statewise
   obstructions.
4. The oriented entrance trace reconstructs the packet and freezes every
   deeper signed path colour.
5. The local hereditary action bound (4.3) closes bounded-fringe repair
   whenever the proposed starting family separately has the linear
   aggregate defect (4.5).
6. On a common SCD/Dyck scaffold in the narrow range
   \(b^2-a^2<\log2\), every valid chronology needs a positive linear
   fraction of top-tag rotor arcs.  If the unmodified scaffold supplies
   only \(o(W)\) of them, Catalan many \(o(m)\)-arc trades fail.

The following is not proved or refuted.

1. A phase-complete, root-scale Catalan trade bank of density above
   (0.7) may have enough owner and entrance supply.
2. Such a bank may solve the grouped integral criterion (6.3) by
   correlating whole cyclic orders.
3. Outside the common-SCD scaffold, no universal top-tag invariant is
   asserted.

Therefore positive-density Catalan/Dyck trades survive only in a sharply
specified form.  Universally, they must be phase-complete, pass the
provider-union cuts at every annular depth, and solve one common coloured
cyclic-order selection.  If they are asked to repair a linear middle-owner
defect, they need \(\Omega(m)\) owner action per Catalan trade on average.
On a common narrow-annulus SCD scaffold with only \(o(W)\) pre-existing
top--top supply, they need \(\Omega(m)\) top-tag arc supply per trade on
average.  Root-scale unrelated packet trades remain outside both local
no-go statements.
Raw root density, fractional orbit balance, or independent trade choices
do not imply any of these properties.
