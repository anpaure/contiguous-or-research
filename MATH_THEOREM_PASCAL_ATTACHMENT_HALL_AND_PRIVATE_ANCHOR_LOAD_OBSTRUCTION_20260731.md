# Pascal-child attachment Hall and the private-anchor load obstruction

Date: 2026-07-31  
Status: exact attachment theorem, exact local packet ledger, and a sharp
scoped obstruction to deriving global `O(m)` resource load from the current
Pascal scalar counts.  No all-parameter dispersed-anchor theorem is claimed.

## 0. Verdict

The actual attachment task/source graph implicit in the four-sector Pascal
construction has a perfect task-saturating matching.  In fact one may use
only the `A-X` shore, and every task receives a distinct source incidence.
Thus the bare attachment congestion is exactly one, not merely `O(1)`.

This does not prove the private-anchor load gate.  A quadratic hexagon menu
has two anchor resources occurring in every option, so literal total token
load is already `Theta(m^2)` at one private source.  These private core
tokens must be omitted from the cross-list conflict count.  More seriously,
one auxiliary slot in the correlated suspended-hex packet has external load

\[
  2m\,\#\{i:P_i\subset R,\ R_i\ne R\}.                 \tag{0.1}
\]

Consequently `O(m)` cross-list load requires a new constant-codegree
representative theorem.  The scalar conclusions of Proposition 3.1 do not
imply it.  A concentrated family of task endpoints forces the count in
(0.1) to be `Omega(m)` for some `R`, and hence forces `Omega(m^2)` auxiliary
slot load.

There is also no proved recurrence bound

\[
                         |U|\le 4\Phi+b_0             \tag{0.2}
\]

with absolute `b_0` for a fully guarded Pascal child.  The coefficient four
is the passive two-coordinate branching bound for an already declared upper
hole.  Residence, new cut/seam packets, and common-cap/compiler reset are
separate rows, and no present theorem bounds their fresh task mass by an
absolute constant.

## 1. Source and one count correction

Use the notation of Sections 3--4 of

```text
MATH_THEORY_K_ALL_BALANCED_TWO_EXTENSION_HEXAGON_AND_O1_REDUCTION_20260731.md
```

Put

\[
 V=[2m-1],\qquad
 W_0={2m-1\choose m},\qquad
 C={2\over m+1}W_0,\qquad U_0=W_0-C.                 \tag{1.1}
\]

The middle owners are

\[
 A_P=P+x+y,\quad X_R=R+x,\quad Y_R=R+y,
\]

where `|P|=m-1` and `|R|=m`.  Proposition 3.1 constructs `C` disjoint path
components, each with one `X` endpoint and one `Y` endpoint.  Write these as

\[
                   X_{R_i},Y_{S_i}\qquad(1\le i\le C). \tag{1.2}
\]

The `R_i` are pairwise distinct, and the `S_i` are pairwise distinct,
because the path components are vertex-disjoint.

There is a small ledger error in item 4 of Proposition 3.1.  At that point
no `A` vertex has yet been used.  The correct unused counts are

\[
       \#A_{\rm unused}=W_0,\qquad
       \#X_{\rm unused}=\#Y_{\rm unused}=U_0.          \tag{1.3}
\]

Only after the opening sentence of Section 4 attaches one distinct `A`
vertex to each of the `C` components does the `A` count become

\[
                         W_0-C=U_0.                    \tag{1.4}
\]

The edge-type calculation in Proposition 4.1 uses the post-attachment
ledger (1.4) and is algebraically correct.

## 2. The exact Pascal task/source graph

There is one attachment task `tau_i` for every component in (1.2).  For
`P in binom(V,m-1)`, define the typed `x`-source incidence

\[
 s_P^x:\quad P+x\ \subset\ P+x+y=A_P.                \tag{2.1}
\]

It is eligible for `tau_i` precisely when

\[
                              P\subset R_i.            \tag{2.2}
\]

Indeed, if `R_i=P+b`, the two incidences through the lower colour `P+x`
contract to the Johnson edge

\[
                         A_P\ --\ X_{R_i}.             \tag{2.3}
\]

The analogous `y`-source `s_P^y:P+y \subset A_P` is eligible when
`P \subset S_i`.  The two typed sources at one `P` share the physical owner
`A_P` and therefore have joint capacity one.

### Theorem 2.1 (load-one Pascal attachment)

The graph between the `C` tasks and the `x`-sources in (2.1)--(2.2) has a
matching saturating every task.  Consequently all `C` components may be
attached on the `A-X` shore using distinct `A` owners, distinct lower
colours, and distinct source incidences.

#### Proof

Let `J` be a set of tasks.  The corresponding `R_i`, `i in J`, are distinct.
Count incidences between these rank-`m` sets and their rank-`(m-1)` facets.
Every `R_i` has exactly `m` facets, so there are `m|J|` incidences.  A fixed
`P in binom(V,m-1)` has exactly `m` rank-`m` supersets in `V`, hence is
incident with at most `m` members of the selected endpoint family.  Thus

\[
                  m|J|\le m|N(J)|,
                  \qquad |N(J)|\ge |J|.               \tag{2.4}
\]

Hall's theorem gives the matching.  If `P_i` is matched to `tau_i`, then
the owners `A_{P_i}`, the colours `P_i+x`, and the incidences `s_{P_i}^x`
are all distinct.  Equation (2.3) supplies the claimed attachments.
\(\square\)

Thus the existence assumption at the opening of Section 4 is automatic if
one permits `p=C` in the notation of Proposition 4.1.  A prescribed mixed
value of `p` is an additional quota problem and is not proved by Theorem
2.1.

This closes the **component-attachment** source graph.  The later buffered
repair blocks (residence, exposed upper witnesses, and compiler sources)
are scaffold-dependent tasks and are not canonically identical to these
`C` components.  For any fixed guarded child, their exact graph is obtained
by joining a repair task `tau` to a source incidence `e` precisely when the
guard-complete, boundary-equivalent packet fibre through `e` has the
required list size.  If this graph is `G_g`, the minimum number of tasks
which must be left exceptional is exactly

\[
 \delta(G_g)=\max_{J\subseteq T}\bigl(|J|-|N_{G_g}(J)|\bigr). \tag{2.5a}
\]

Indeed this is the deficiency form of Hall's theorem.  Thus at most `h`
exceptions are possible if and only if `delta(G_g)<=h`.  Current Pascal
theorems do not define all edges of `G_g`, so Theorem 2.1 must not be cited
as Hall for those later repair tasks.

For completeness, on the two-shore source ground

\[
 \mathcal S=\{s_P^x,s_P^y:P\in{V\choose m-1}\},       \tag{2.5}
\]

let `M_A` be the partition matroid whose blocks are
`{s_P^x,s_P^y}` and whose block ranks are one.  Rado's theorem says that a
task-saturating source assignment respecting the common `A_P` capacities
exists exactly when

\[
                         r_{M_A}(N(J))\ge |J|
                         \qquad(J\subseteq[C]).        \tag{2.6}
\]

Theorem 2.1 proves (2.6) by restricting to the `x`-sources.  Exact side
quotas require an extra weighted or flow condition; they are not part of
ordinary Rado.

## 3. Exact raw incidence-hexagon ledger

Fix an `x`-source `s_P^x`.  In the standard incidence hexagon take

\[
                 C_0=P+x,\qquad a=y,                 \tag{3.1}
\]

choose

\[
                 b\in P+x,\qquad c\in V\setminus P, \tag{3.2}
\]

and use the six vertices

\[
 C_0, C_0+y, C_0-b+y, C_0-b+y+c, C_0-b+c, C_0+c. \tag{3.3}
\]

There are exactly `m^2` parameter pairs `(b,c)`.  The per-source
multiplicities are as follows.

| role | token form | multiplicity of one token |
|---|---|---:|
| private lower core | `P+x` | `m^2` |
| private owner core | `P+x+y` | `m^2` |
| first auxiliary lower, `b=x` | `P+y` | `m` |
| first auxiliary lower, `b=u in P` | `P-u+x+y` | `m` |
| first auxiliary owner, `b=x` | `P+c+y` | `1` |
| first auxiliary owner, `b=u in P` | `P-u+c+x+y` | `1` |
| second auxiliary lower, `b=x` | `P+c` | `1` |
| second auxiliary lower, `b=u in P` | `P-u+c+x` | `1` |
| second auxiliary owner | `P+c+x` | `m` |

The two private core tokens show that **literal total** token load cannot be
`O(m)`: even one quadratic list gives load `m^2`.  For conflict bounds the
correct quantity is task-relative external load

\[
 \ell_{\rm ext}(r,i)
   =\sum_{j\ne i}\#\{p\in\mathcal P_j:r\in R(p)\}.    \tag{3.4}
\]

Under Theorem 2.1 the private cores are distinct, so their same-list
`m^2` multiplicity contributes zero to (3.4), unless they occur
auxiliarily in another task's menu.

For a selected source family `F subset binom(V,m-1)`, define

\[
 d_-(Q)=\#\{P\in F:Q\subset P\}
       \quad(Q\in{V\choose m-2}),                    \tag{3.5}
\]

\[
 d_+(R)=\#\{P\in F:P\subset R\}
       \quad(R\in{V\choose m}),                      \tag{3.6}
\]

and let `d_J(P')` be the number of members of `F` Johnson-adjacent to `P'`.
Then

\[
 d_J(P')\le
 \min\{(m-1)\max_Qd_-(Q),\ m\max_Rd_+(R)\}.          \tag{3.7}
\]

The table gives the following exact worst fibres:

\[
 \begin{array}{c|c}
 \text{auxiliary token}&\text{load contribution}\\ \hline
 Q+x+y& m d_-(Q)\\
 R+x\text{ as the last owner}&m d_+(R)\\
 P'+x\text{ or }P'+x+y\text{ after a swap}&d_J(P')\\
 R\text{ or }R+y&d_+(R).
 \end{array}                                         \tag{3.8}
\]

Consequently bounded upper and lower codegrees in (3.5)--(3.6) are a
sufficient raw physical/colour condition for `O(m)` external load.  They are
not consequences of injectivity of `F`.

## 4. The first correlated-C6 auxiliary-slot obstruction

The attachment (2.3) is the diamond atom

\[
 A_i=(D_i,V_i;A_{P_i},X_{R_i}),\qquad
 D_i=P_i+x,\quad V_i=R_i+x+y,                         \tag{4.1}
\]

where `R_i=P_i+b_i`.  Because the `P_i` and `R_i` are separately distinct,
the four target resources in (4.1) are pairwise private across tasks.

The suspended transparent-hex identity from

```text
MATH_THEOREM_CATALAN_SUSPENDED_TRANSPARENT_HEX_ABSORBER_AND_BLOCKERS_20260731.md
```

is local and applies with deletion coordinate `u in D_i`, exterior
coordinate `c notin V_i`, and the two orientations of `{b_i,y}`.  On the
odd ground set of size `2m+1` this gives

\[
                         2m(m-1)                       \tag{4.2}
\]

formal phase pairs through (4.1).  The even-host theorem's `2n(n-2)` count
changes only because the odd host has `m-1`, rather than `m-2`, exterior
coordinates; the local resource identity is unchanged.

One of the six literal slots in every such packet is

\[
                         D_i+c=P_i+x+c.                \tag{4.3}
\]

For fixed `c`, it is independent of `u` and of the orientation, so it
occurs in exactly `2m` options from task `i`.  Therefore, for a core
rank-`m` set `R`, the contribution to the slot at `X_R=R+x` is exactly

\[
  2m\,d_{\rm ext}(R),\qquad
  d_{\rm ext}(R)=
       \#\{i:P_i\subset R,\ R_i\ne R\}.               \tag{4.4}
\]

Indeed `c=R-P_i` is exterior to `V_i=R_i+x+y` exactly when `R != R_i`.
Other packet roles may add more load, so (4.4) is in particular a lower
bound on complete token load.

Thus the claimed global `O(m)` bound requires

\[
                         \max_Rd_{\rm ext}(R)=O(1).     \tag{4.5}
\]

This necessary condition is already outside the ordinary Hall theorem of
Section 2.

## 5. A concentrated endpoint counterexample

Let `W subset V` have size

\[
                         |W|=m+s,                      \tag{5.1}
\]

and take as task endpoints every

\[
                         R_i\in{W\choose m}.           \tag{5.2}
\]

For each task choose an arbitrary facet `P_i subset R_i`; repetitions are
allowed for this lower bound.  Every selected `P_i` lies in exactly `s+1`
members of `binom(W,m)`, one of which is its own `R_i`.  Double counting
the pairs `(i,R)` with `P_i subset R` and `R ne R_i` gives

\[
 \sum_{R\in{W\choose m}}d_{\rm ext}(R)
       =s{m+s\choose m}.                              \tag{5.3}
\]

There are `binom(m+s,m)` terms in the sum, so

\[
                         \max_Rd_{\rm ext}(R)\ge s.    \tag{5.4}
\]

By (4.4), some auxiliary slot has load at least `2ms`.

For the unpruned suspended-hex lists, `L=2m(m-1)`.  The task whose endpoint
is this maximizing `R` contains `X_R` in every candidate, while other lists
contribute at least `2ms` candidates containing the same slot.  Hence its
conflict degree satisfies `Delta>=2ms`, and Haxell's sufficient inequality
`L>=2Delta` would require

\[
                              m-1\ge2s.                \tag{5.4a}
\]

The choice (5.5) violates (5.4a) for all sufficiently large `m`.  This is a
failure of the unpruned Haxell certificate, not a proof that no carefully
pruned independent transversal exists.

This obstruction fits below the Catalan task count while keeping
`s=Omega(m)`.  Let

\[
 t=\left\lceil\log_2{m+1\over2}\right\rceil,
 \qquad |W|=2m-1-t,
 \qquad s=m-1-t.                                     \tag{5.5}
\]

Since

\[
 {2m-1-t\choose m}/{2m-1\choose m}
 =\prod_{j=0}^{t-1}{m-1-j\over2m-1-j}
 \le2^{-t}\le {2\over m+1},                          \tag{5.6}
\]

the family (5.2) has at most

\[
                         C={2W_0\over m+1}             \tag{5.7}
\]

tasks.  It may therefore occur as a subfamily of a `C`-element distinct
endpoint ledger, while (5.4) is `m-O(log m)` and the forced slot load is
`Omega(m^2)`.

This is a scoped obstruction: it proves that the **cardinality and
distinct-endpoint conclusions** of Proposition 3.1 do not imply the load
gate.  It does not assert that this concentrated endpoint family has already
been realized by a complete old-colour-exact `U`-path/bridge bank.  A
positive theorem may use additional dispersion forced by such a bank, but
that dispersion must be stated and proved.

## 6. Why this is not an ordinary Rado corollary

The desired representative system may be written with binary variables
`z_(i,P)` as

\[
 \sum_{P\subset R_i}z_{i,P}=1,\qquad
 \sum_i z_{i,P}\le1,                                  \tag{6.1}
\]

together with the resource rows

\[
 \sum_{i,P\subset R}z_{i,P}\le\lambda_+,qquad
 \sum_{i,Q\subset P}z_{i,P}\le\lambda_-              \tag{6.2}
\]

for every rank-`m` set `R` and rank-`(m-2)` set `Q`.  Equation (6.1) alone
is the Hall theorem of Section 2.  The overlapping rows (6.2) are not a
partition or laminar matroid.

Already for `m=3`, upper capacity one on the ground `binom([5],2)` says
that the selected two-sets form a matching in `K_5`: two selected pairs
cannot share a point, because their union is a rank-three cap.  This
independence system is not a matroid.  For example

\[
                         I=\{12,34\},\qquad J=\{13\}   \tag{6.3}
\]

are independent and `|I|>|J|`, but neither member of `I-J` can augment
`J`.  The matroid exchange axiom fails.

Therefore no unspecified Rado rank can certify (6.1)--(6.2).  A positive
result needs a special bounded-codegree representative theorem (or a
stronger structured endpoint hypothesis).  The concentrated set `W` gives
an exact necessary capacity cut for any such theorem.

## 7. Audit of the proposed `|U| <= 4 Phi+b_0` salvage

Equation (5.1) of

```text
MATH_THEOREM_BUFFERED_HEXAGON_LLL_REDUCTION_AND_MISSING_LOAD_GATE_20260731.md
```

introduces

\[
                         |U|\le4\Phi_k+b_0             \tag{7.1}
\]

as a supposition.  It is the only occurrence of this bound in the current
corpus.  The closest general recurrence is equation (5.1) of

```text
MATH_THEOREM_REGENERATIVE_GUARDED_SWITCH_CONTRACTION_AND_CONSTANT_ADDITIVE_20260731.md
```

namely

\[
       \|\widehat\Pi_{k'}\|_1\le\lambda\|\Pi_k\|_1+b_0,         \tag{7.2}
\]

and that theorem explicitly assumes both `lambda` and `b_0`.

The proved Pascal identities are separated in Section 4 of

```text
MATH_THEOREM_BOUNDED_DEFECT_REGENERATIVE_SPINE_AND_EXPLICIT_O1_CONSTANT_20260731.md
```

as follows.

1. **Central row.**  On a supplied legal perfect trace/owner transition,
   exact central ownership maps `0 -> 0`; this is (4.2).  This does not
   count the other tasks.
2. **Residence row.**  Every proper positive run loses exactly one unit,
   (4.4).  A plateau step needs one extra parent unit or an explicit
   compensation packet.  The number of new compensation tasks is not
   bounded by central defect.
3. **Upper row.**  Fully internal protected occurrences transport by
   (4.6)--(4.7).  A passively carried upper hole can have two descendants
   per new coordinate, hence four over a two-coordinate odd step.  This is
   the valid scope of the coefficient four.  Cut and seam casualties still
   require the separate kernel-mass bound (4.8).
4. **Compiler/common-cap row.**  Section 4.4 states that no functorial
   parent-to-child cap map is proved; this row must be reset after the child
   chronology is fixed.

The last point has a literal logical obstruction.  Section 5.2 of

```text
MATH_THEOREM_ALLK_OWNER_FACTOR_BOUNDED_DEFECT_PHYSICALIZATION_20260731.md
```

gives disjoint robust-Hall interface gadgets, each forcing at least one
common-cap hole.  Repeating the gadget makes compiler debt grow with the
number of copies despite uniform marginal expansion.  This is an abstract
compiler-interface obstruction, not a literal all-`k` carrier no-go, but it
refutes any deduction of absolute `b_0` from central inheritance and
marginal Hall alone.

The same file records the exact residence tax and states that no theorem
currently bounds all-depth defects or the exact compiler boundary uniformly
in `k`.  The fixed `K17` calibration has thousands of short-run and upper
defects before the compiler is reached; these finite counts do not prove
asymptotic growth, but they rule out treating the missing rows as an
automatic absolute sidecar.

Hence (7.1) becomes proof-safe only after `Phi` is defined to charge all
four carried rows and one separately proves:

\[
 \begin{array}{l}
 \text{fresh residence/compensation tasks}=O(1),\\
 \text{fresh cut/seam upper casualties}=O(1),\\
 \text{fresh compiler/common-cap reset debt}=O(1),
 \end{array}                                             \tag{7.3}
\]

uniformly on the same guarded Pascal state.  No present theorem supplies
(7.3).

## 8. Exact remaining theorem

The attachment part is closed.  The remaining private-anchor statement is:

> For the **actual** `C` Pascal component endpoints, choose the Hall
> representatives `P_i subset R_i` so that the target atoms (4.1) possess
> quadratic guard-complete packet lists, the selected source family has
> bounded upper and lower codegrees, every physical/colour auxiliary token
> has external load `O(m)`, and every cap-ticket token has external load
> `O(m)` after the complete paths are included.

The correlated-C6 planting theorem does not prove this statement.  It gives
the local packet identity, exact target coherence cuts, and a prepacked
linear resource-private bank, but not quadratic lists at every Pascal task
with the global dispersion above.  Cap-ticket load is especially absent:
the raw incidence hexagon does not determine the external mate incidences,
alternating paths, or sink-capacity tokens of a whole child packet.
