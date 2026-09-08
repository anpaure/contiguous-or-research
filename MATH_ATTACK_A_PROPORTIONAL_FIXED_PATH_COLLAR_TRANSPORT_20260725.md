# Proportional atoms after central conditioning: exact collar cuts and the ordered-intersection gate

Date: 2026-07-25

This note tests the proposed two-stage argument

1. resolve the vertical/central part by whole tight paths;
2. use the remaining \(O(m^{-2})\) non-cover overlap to round endpoint
   collars.

There is one positive endpoint theorem: every sufficiently small family of
free rank-\((m-1)\) endpoints has a facet SDR.  The proposed global
conclusion nevertheless does not follow in the canonical same-start
column.  Central conditioning freezes a
\((1-o(1))\)-fraction of every fixed-window row, and on the explicit
first-avoided-pair path forest the first new constraint is the ordered
rank-\((m-2)\) histogram

\[
             T_i=S_i\cap S_{i-1}.
\]

This histogram is fixed on all but \(O(J)\) positions.  A Boolean nested
flow may choose an arbitrary facet of \(S_i\); a physical continuation must
choose the facet prescribed by the preceding path colour.  The resulting
capacity cuts are proved below.  They are not controlled by the
unconditioned \(O(m^{-2})\) codegree sum.

Scope: a full Pascal corridor may choose left/right endpoint deletions and
extensions at every depth.  Those choices can change bulk descendants.
The ordered-intersection cuts below are exact for the canonical outgoing
column and for transporting a prechosen abstract flow onto that column;
they are not a no-go against every full-corridor rerouting.

## 1. A fixed central segment has a deterministic core

Put

\[
n=2m+1,\qquad W=\binom nm,
\qquad N_q=\binom n{m+q},
\]

and use the proportional atom notation of
`PROPORTIONAL_TIGHT_ATOM_GAUSSIAN_REDUCTION_20260725.md`.  Let \(R\) be a
realizable \(b\)-start central ladder, and let \({\cal C}(R)\) be the family
of all two-sided tight-word completions of that ladder.  Define its fixed
core by

\[
D(R)=\bigcap_{E\in\mathcal C(R)}E,
\tag{1.1}
\]

where only designated fixed-window targets are retained in the
intersection.

### Proposition 1.1 (fixed-core obstruction)

For every signed depth \(q\), the core \(D(R)\) contains at least

\[
             b_q-(|q|+1)
\tag{1.2}
\]

of the designated depth-\(q\) targets.  Hence, on a window
\(|q|\le K=A\sqrt m\),

\[
 |D(R)|\ge \sum_{|q|\le K}b_q-O_A(m)
          =(1-O_A(m^{-1/4}))\sum_{|q|\le K}b_q.
\tag{1.3}
\]

If \(R_1,\ldots,R_s\) are pairwise central-disjoint ladders and
\(G_D\) is the graph in which \(ij\) is an edge when
\(D(R_i)\cap D(R_j)\ne\varnothing\), then every family of pairwise
target-disjoint completions uses an independent set of \(G_D\).  In
particular it discards at least \(\tau(G_D)\) ladders.

#### Proof

The first assertion is exactly the central-ladder rigidity identity.  If
\(q=-d\), every start \(i\ge d\) is determined by the central ladder; if
\(q=d\), every start \(i\le b-d\) is determined.  Intersecting with the
chosen start set loses at most \(d+1\) positions.

On a fixed Gaussian window, \(b_q=\Theta_A(b)\), so the main sum in
(1.3) is \(\Theta_A(b\sqrt m)=\Theta_A(m^{5/4})\), while
\(\sum_{q\le K}O(q)=O_A(m)\).  This proves (1.3).

Every completion of \(R_i\) contains \(D(R_i)\).  Thus two ladders joined
in \(G_D\) cannot both be completed inside a matching.  The vertex-cover
statement follows. \(\square\)

There is a useful audit consequence.  If degrees are recomputed inside
one completion fibre \({\cal C}(R)\), then for every
\(v,w\in D(R)\),

\[
       \frac{\deg_R(v,w)}{\deg_R(v)}=1.
\tag{1.4}
\]

Thus the unrestricted \(O(m^{-2})\) non-cover row sum is not inherited by
the conditioned completion fibre.  It becomes maximally concentrated on
the deterministic core.

## 2. Ordered intersections on a tight path

Consider one oriented tight component with consecutive middle windows

\[
 X_i=I_\pi(t+i,m)\qquad(0\le i<\ell).
\tag{2.1}
\]

At an endpoint the coordinate order may be continued by a collar.  Put

\[
 S_i=X_i\cap X_{i-1}=I_\pi(t+i,m-1).
\tag{2.2}
\]

The \(S_i\)'s are the outgoing rank-\((m-1)\) colours in the orientation
used in the first-avoided-pair extraction.

### Lemma 2.1 (ordered-intersection rigidity)

Whenever the displayed windows needed on the right lie inside the
selected component,

\[
 L_q(X_i):=I_\pi(t+i,m-q)
   =\bigcap_{h=0}^{q}X_{i-h}
   =\bigcap_{h=0}^{q-1}S_{i-h}.
\tag{2.3}
\]

Consequently, in a forest of \(J\) tight components, at most \(qJ\)
lower depth-\(q\) owner positions can depend on endpoint collars.  In
particular, away from those endpoints,

\[
                  L_2(X_i)=S_i\cap S_{i-1}.
\tag{2.4}
\]

The analogous upper statement holds with unions and the opposite
endpoints.

#### Proof

The largest left endpoint among
\(X_i,X_{i-1},\ldots,X_{i-q}\) is \(t+i\), and the smallest right
endpoint is \(t+i+m-q-1\).  Their intersection is therefore the first
interval in (2.3).  The second equality follows in the same way from
(2.2).  Only the first \(q\) positions of a component can use a window
outside the selected component. \(\square\)

This is the exact ordering constraint.  Abstract nesting allows any
facet of \(S_i\) at the next depth.  Once the tight path is fixed, the
interior facet is the unique set \(S_i\cap S_{i-1}\).

## 3. Exact balanced-transport cuts

Let \(\Omega\) be a set of \(M\) middle owners lying on a tight path
forest, and let \(B_q\le qJ\) be the number of lower depth-\(q\) positions
which touch collars.  On the remaining positions define the fixed
histogram

\[
 \rho_q(T)=\#\{X\in\Omega:\ X\text{ is interior at depth }q,
                         \ L_q(X)=T\}.
\tag{3.1}
\]

Let \(P_q\) be a balanced nested resolution of all \(W\) middle owners,
so every rank-\((m-q)\) target has \(P_q\)-fibre size \(c_q\) or
\(c_q+1\), where

\[
 c_q=\left\lfloor\frac{W}{\binom n{m-q}}\right\rfloor.
\tag{3.2}
\]

Write

\[
 e_q=\#\{X\in\Omega:L_q(X)\ne P_q(X)\},
 \qquad R=W-M.
\tag{3.3}
\]

### Theorem 3.1 (interior overload and deficit cuts)

For every depth \(q\),

\[
 \boxed{
 e_q\ge
   \sum_T\bigl(\rho_q(T)-(c_q+1)\bigr)_+ ,}
\tag{3.4}
\]

and

\[
 \boxed{
 e_q+R+B_q\ge
   \sum_T\bigl(c_q-\rho_q(T)\bigr)_+ .}
\tag{3.5}
\]

These inequalities hold for every choice of endpoint collars and every
choice of the omitted-owner flags.

#### Proof

Fix \(T\).  Among the \(\rho_q(T)\) interior owners whose physical flag
is \(T\), at most \(c_q+1\) can also satisfy \(P_q(X)=T\), because this
is the global upper fibre capacity.  The remaining owners are errors.
Summing over the disjoint physical fibres proves (3.4).

The resolution assigns at least \(c_q\) owners to each \(T\).  At most
\(\rho_q(T)\) of those assignments can come correctly from the fixed
interior fibre.  A missing unit must therefore come from an omitted owner,
a collar position, or an interior owner counted as an error.  Each such
owner supplies at most one unit at this depth.  Summation gives (3.5).
\(\square\)

Thus a common nested Hall flow can be transported onto the canonical
columns of fixed rows only if their ordered-intersection histograms already
satisfy the two displayed cuts.  The flow does not create new choices
inside that canonical column.

## 4. The first obstruction is already at depth two

Apply Theorem 3.1 to the path forest of Theorem 5.1 in
`PAIR_OMISSION_TIGHT_ROW_MULTICOVER_20260725.md`.  Here

\[
 M=N_1=\binom n{m-1}=\frac{m}{m+2}W,
 \qquad R=W-N_1=\frac{2W}{m+2},
\tag{4.1}
\]

and put \(N_2=\binom n{m-2}\).  For \(m\ge8\),

\[
 1<\frac{W}{N_2}
   =\frac{(m+2)(m+3)}{m(m-1)}<2,
\tag{4.2}
\]

so \(c_2=1\).  Let

\[
 \rho_2(T)=\#\{i\text{ interior}:S_i\cap S_{i-1}=T\}.
\tag{4.3}
\]

### Corollary 4.1 (near-rainbow ordered-intersection requirement)

Every transported balanced resolution satisfies

\[
 e_2\ge\sum_T(\rho_2(T)-2)_+,
\tag{4.4}
\]

and

\[
 e_2+\frac{2W}{m+2}+2J
 \ge \#\{T:\rho_2(T)=0\}.
\tag{4.5}
\]

The harmless \(2J\) in (4.5) allows either endpoint convention; one
orientation gives the sharper \(B_2\le2J\), and in the usual outgoing
lower convention only one new colour per component is needed.

In particular, if \(e_2=o(W)\), then both the number of missing
rank-\((m-2)\) targets and the total collision excess

\[
       \sum_T(\rho_2(T)-1)_+
\tag{4.6}
\]

are \(o(W)\), because \(J=O(W\log^2m/m)=o(W)\) and
\(N_1-N_2=O(W/m)\).

#### Proof

Equations (4.4)--(4.5) are (3.4)--(3.5).  For the last assertion use the
integer identity

\[
 \sum_T(\rho_2(T)-1)_+-\#\{T:\rho_2(T)=0\}
   =\sum_T(\rho_2(T)-1)
   =|I_2|-N_2,
\tag{4.7}
\]

where \(|I_2|=N_1-O(J)\) is the number of interior positions. \(\square\)

Theorem 5.1 proves that every \(S\in\binom{[n]}{m-1}\) occurs exactly
once.  It proves no estimate for the ordered intersections in (4.3).
Hence (4.4)--(4.5), not rank-\((m-1)\) Hall, are the first unverified
cuts.

## 5. What endpoint Hall does prove

At a genuinely free lower endpoint with prescribed
\(S\in\binom{[n]}{m-1}\), every facet \(T\in\partial S\) can be realized
as the depth-two flag by a two-window collar.  Indeed, if
\(X\setminus S=\{a\}\) and \(S\setminus T=\{b\}\), choose distinct
\(y,z\notin X\) and use the consecutive middle windows

\[
       T\cup\{y,z\},\qquad S\cup\{y\},\qquad X.
\tag{5.1}
\]

Their consecutive differences have disjoint supports, so they form an
injective tight collar.

### Proposition 5.1 (unconstrained endpoint facet SDR)

Let \({\cal E}\subseteq\binom{[n]}{m-1}\) be a family of distinct free
endpoint colours satisfying

\[
       |{\cal E}|\le\binom{2m-3}{m-1}.
\tag{5.2}
\]

Then there is an injection \(f:{\cal E}\to\binom{[n]}{m-2}\) with
\(f(S)\subset S\) for every \(S\).  In particular this applies to the
\(O(J)\) endpoint colours of the first-avoided-pair forest for all large
\(m\).

#### Proof

For every \({\cal A}\subseteq{\cal E}\), write
\(|{\cal A}|=\binom{x}{m-1}\) in the Lovasz form.  Assumption (5.2)
gives \(x\le2m-3\).  Kruskal--Katona yields

\[
 |\partial{\cal A}|\ge\binom{x}{m-2}
  =\binom{x}{m-1}\frac{m-1}{x-m+2}
  \ge|{\cal A}|.
\tag{5.3}
\]

Hall's theorem supplies the injection.  Finally
\(J/W=O(\log^2m/m)=o(1)\), while the binomial coefficient in (5.2) is
a fixed positive asymptotic fraction of \(W\). \(\square\)

The same proof has a useful robust form.

### Corollary 5.2 (forbidden-facet loss is at most its cardinality)

Under the hypotheses of Proposition 5.1, let
\({\cal F}\subseteq\binom{[n]}{m-2}\) be any set of already saturated
facets.  Then at least

\[
                 |{\cal E}|-|{\cal F}|
\tag{5.4}
\]

members of \({\cal E}\) can be assigned distinct facets outside
\({\cal F}\).

#### Proof

For every \({\cal A}\subseteq{\cal E}\), Proposition 5.1 gives

\[
 |{\cal A}|-|\partial{\cal A}\setminus{\cal F}|
 \le |\partial{\cal A}\cap{\cal F}|
 \le |{\cal F}|.
\]

The deficiency form of Hall's theorem says that the number of unmatched
left vertices in a maximum matching is the maximum of the left side over
all \({\cal A}\). \(\square\)

This is the precise positive use of Boolean shadow expansion.  It makes
the free collars mutually distinct when every child has a spare capacity
unit.  More generally, Corollary 5.2 loses only the number of saturated
children.  It does not bound that number for the deterministic interior.

To see the remaining condition exactly, let \(u(T)\) be the residual
capacity of a rank-\((m-2)\) target after the interior and omitted-owner
assignments have been fixed.  The endpoint choice is a capacitated
bipartite matching, and its upper Hall inequalities are

\[
 \boxed{
 |{\cal A}|\le\sum_{T\in\partial{\cal A}}u(T)
 \quad({\cal A}\subseteq{\cal E}).}
\tag{5.5}
\]

Together with the analogous lower-demand cuts, these are sufficient by
integral lower-bounded flow.  Shadow expansion proves (5.5) when
\(u(T)\ge1\) throughout the relevant shadow; it says nothing when the
fixed interior has saturated that shadow.  The first possible failed cut
is already a singleton endpoint \(S\) with

\[
                 u(T)=0\quad(T\in\partial S).
\tag{5.6}
\]

At greater depths the same statement is a common nested lower-bounded
flow through the endpoint collars, with residual capacities obtained by
subtracting the fixed ordered-intersection histograms.  Integrality is
automatic once its cuts hold; the missing assertion is the cut slack.

## 6. Why the \(m^{-2}\) estimate does not prove the cut slack

For two unrestricted slots whose set differences satisfy \(a+c\ge2\),
the normalized conditional overlap is \(O(m^{-2})\).  At depth two the
ordered pair \((S_i,S_{i-1})\) has \(a=c=1\), so it belongs to that
non-cover scale before conditioning.  The path forest, however, conditions
on one particular Johnson neighbour \(S_{i-1}\) for essentially every
\(S_i\).  After that conditioning,

\[
       \Pr(S_i\cap S_{i-1}=T_i\mid\text{the fixed path})=1.
\tag{6.1}
\]

Thus the \(m^{-2}\) statement controls the probability that an
unrestricted second row contains a specified second target after a first
collision.  It does not control the histogram of the one neighbour
deliberately selected at every vertex of a fixed path forest.  Equations
(1.4) and (6.1) are two forms of the same conditioning loss.

Nor can endpoint alteration change this conclusion: at depth \(q\) it
has variables at only \(O(qJ)\) positions, while (2.3) fixes all the
others.  Any LLL or alteration theorem must therefore take (3.4)--(3.5)
as hypotheses; they cannot be deduced from the unconditioned codegree
sum.

## 7. Proved boundary

The route yields the following rigorous conclusions.

1. Central conditioning freezes a \((1-O_A(m^{-1/4}))\)-fraction of every
   proportional fixed-window atom.  Completion fibres do not retain the
   \(O(m^{-2})\) row-sum estimate.
2. On the explicit q1-saturating path forest, canonical outgoing flags are
   the ordered intersections (2.3), except at \(O(qJ)\) endpoint
   positions.
3. The exact canonical-column balanced-transport cuts are (3.4)--(3.5).
   At the first new depth they require the ordered q1 word to be
   near-rainbow under \(S_i,S_{i-1}\mapsto S_i\cap S_{i-1}\).
4. Free endpoint facets do have an integral SDR by Proposition 5.1.
   Avoiding a forbidden facet set loses at most its cardinality by
   Corollary 5.2.  With occupied interior targets, the minimal remaining
   inequality is the residual capacitated shadow cut (5.5), and at all
   depths its common nested analogue.

No constant-one theorem follows from the present argument.  In the
canonical-column sublane, the smallest unproved positive statement is that
the fixed ordered-intersection histograms leave enough residual capacity
to satisfy (5.5) and its simultaneous nested versions with aggregate
labelled error \(o(W)\).  In the full corridor, the corresponding gate is
to orient the evolving same-row two-parent incidence graphs with \(o(W)\)
cumulative component excess.  Proving either statement requires control of
the actual row ordering; Boolean marginals and the unrestricted
\(O(m^{-2})\) overlap do not supply it.
