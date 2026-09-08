# Global certificate-incidence packets: exact failed-literal descent and the finite halo alternative at FL30

Date: 2026-07-29  
Lane: K  
Status: theorem plus independently replayed frozen chain  
Scope: fixed resident endpoint, degree-two physical packet libraries preserving complete lower and upper q1 support

Live-frontier notice: the historical descent continued through detector zero.
The successor theorem is
`MATH_THEOREM_K_K16_FL0_MOTIF390_FARKAS_LOCK_AND_MINIMAL_CERTIFICATE_EXPANSION_20260729.md`,
which gives the solver-free FL0 Farkas lock and the unique full-q1 two-edge
portal.  Nothing below should be read as the current terminal obstruction.

## 1. Result

The former integer-descent theorem is sharpened in three ways.

First, every legal packet has an exact birth--death ledger on signed failed
literal tokens:

\[
\Phi(Q^T)-\Phi(Q)
 =\#\{\text{failures born}\}-\#\{\text{failures killed}\}.
\]

Second, the mechanism used after the first \(Q_{73}\to Q_{69}\) smallest-core
step is formalized exactly.  It is not a weighted dual or a packet-gain
theorem.  Each old failure puts unit weight on every present removable edge
appearing in the union of its two frozen branch proofs; the nine heaviest
edges are used only as a **global certificate-incidence focus**.  Connected
alternating \(C_4,C_6,C_8\) packets through that focus are then scored by a
complete new failed-literal audit.  The frozen, independently replayed prefix
is

\[
73\longrightarrow69\longrightarrow56\longrightarrow48
\longrightarrow39\longrightarrow34\longrightarrow30,
\]

with deaths \(4,13,8,9,5,4\) and no births.  Every state is degree two and
has complete lower and upper q1 support.

Prepending the independently frozen prefix from the predecessor report gives
the requested combined chain

\[
93\to86\to81\to78\to76\to73\to69\to56\to48\to39\to34\to30.
\]

Third, positive proof-incidence weight does **not** imply descent.  At
\(Q_{30}\), two legal packets with the identical incidence signature
\((W,H)=(7,7)\) give scores 27 and 34.  Thus the incidence rule is a search
focus, not a Lyapunov certificate.  What is true, and sufficient for
proof-directed descent, is the following exact finite alternative:

1. exhibit one legal q1-support-complete packet whose complete new bank is
   smaller; or
2. for every packet in a declared finite library, give either an ordinary
   unit contradiction or enough transported/new exact eligibility and
   branch-unit-propagation transcripts to prove that its bank is at least as
   large; each transcript also yields a Farkas certificate as an audit check.

This alternative is necessary and sufficient for library-local minimality.
It admits a proof-halo compression: packets preserving a frozen certificate
atlas transport the old failed literals automatically, so only halo-changing
packets require fresh branch certificates.

At the frozen FL30 endpoint the positive alternative occurs.  The complete
global-top-nine library has 64 connected q1-support-complete packets of radii
two through four.  Thirteen improve the score and nine attain score 27.  The
materialized best \(C_6\) preserves 27 old failed literals, destroys exactly
three, and creates none:

\[
30-3+0=27.
\]

This is an exact instance of the gain/loss theorem.  It proves that FL30 is
not the first stall.  It is not a universal existence theorem, and no
convergence claim is made.

## 2. Exact failed-literal bank

Throughout this note, a packet is called **q1-support-complete** when it is a
simple spanning degree-two factor and every one of the 11,440 physical lower
q1 targets and every one of the 11,440 physical upper q1 targets retains load
at least one.  This does not assert that the q1 load vector, provider
multiset, residence, deeper shadows, or compiler data are unchanged.

For a q1 factor \(Q\) and fixed resident factor \(R\), let
\(\Sigma(Q,R)\) be the complete finite signed-cardinality system consisting
of:

- both endpoint-degree inequalities;
- all lower- and upper-q1 support rows;
- every current short-run motif row;
- Boolean bounds.

Run the frozen deterministic signed unit propagation.  Assume first that it
reaches a fixpoint \(\sigma_Q\), rather than a contradiction.

For a motif row \(M\), delete variables already fixed to zero and call the row
hit if some variable is fixed to one.  Define the two-choice eligibility bank

\[
E(Q)=\{v:\sigma_Q(v)=*,\ 
  v\text{ lies in an unhit motif with exactly two live variables}\}.
\tag{2.1}
\]

For \(v\in E(Q)\), let \(U_Q(v=\varepsilon)\) be unit propagation after the
single Boolean assumption \(v=\varepsilon\).  Variables are occurrence-side
signed tokens: the same physical edge on the `red_add` and `blue_remove`
shores is not identified.  The complete failed-literal bank is

\[
F(Q)=\{v\in E(Q):
 U_Q(v=0)=\bot=U_Q(v=1)\},
\tag{2.2}
\]

and

\[
\Phi(Q)=|F(Q)|.
\tag{2.3}
\]

The bank is defined only after ordinary unit propagation reaches a fixpoint.
An endpoint with an ordinary unit contradiction is already infeasible by a
stronger detector and is not assigned a finite lower score here.

An **exact branch-UP contradiction transcript** \(\Pi_v^\varepsilon\) is the
ordered deterministic propagation record after assuming
\(v=\varepsilon\).  Every step stores the normalized forcing row, its entire
variable/coefficient support, the values fixed before the step, the residual
Boolean minimum/maximum or slack calculation, and the uniquely forced
literal.  The last step stores the complete contradictory row and residual
bound.  Replaying this ordered record is what proves
\(U_Q(v=\varepsilon)=\bot\).

### Lemma 2.1 (a branch-UP transcript yields a Farkas packet)

Every contradiction in (2.2) has a finite nonnegative-integer linear
combination of the used signed rows, Boolean bounds, and the branch assumption
which yields \(0\le-c\) for an integer \(c\ge1\), equivalently a finite
nonnegative-rational combination which yields

\[
0\le-1.
\tag{2.4}
\]

#### Proof

When a signed row is tight at its Boolean minimum, each unassigned variable in
that row is forced to its minimizing value.  Combining the row with the
bounds and previously derived forced equalities gives the corresponding
literal inequality.  Induction along the finite propagation provenance
derives every assigned literal.  At the contradictory row, substitute these
derived inequalities and combine once more.  All multipliers are
nonnegative integers because every propagation step adds signed
unit-coefficient inequalities.  The result has zero left side and a negative
integer right side \(-c\), \(c\ge1\).  Dividing all multipliers by \(c\)
gives (2.4). \(\square\)

Thus a failed-literal certificate for \(v\) consists of

\[
\mathfrak c_v=(E_v,\Pi_v^0,\Pi_v^1;
                    \Lambda_v^0,\Lambda_v^1),
\tag{2.5}
\]

where \(E_v\) proves the exact eligibility statement (2.1) from the complete
fixpoint, \(\Pi_v^\varepsilon\) is the exact ordered branch-UP contradiction
transcript, and \(\Lambda_v^\varepsilon\) is its derived Farkas packet
(2.4).  The transcript proves membership in the algorithmic bank; the
Farkas packet alone proves semantic infeasibility but is not sufficient to
prove that unit propagation detects it.

## 3. Exact packet gain/loss identity

Let \(T:Q\mapsto Q'\) be a legal physical packet: \(Q'\) is again degree two
and has complete lower and upper q1 support.  Identify variables by their
signed physical keys `(red_add, edge)` or `(blue_remove, edge)` whenever the
same key exists in both systems.

Put

\[
K_T=F(Q)\setminus F(Q'),
\qquad
B_T=F(Q')\setminus F(Q).
\tag{3.1}
\]

Thus \(K_T\) is the exact set of killed signed failure tokens and \(B_T\) is
the exact set of born signed failure tokens.  These are defined from the two
complete banks, not from whether one frozen proof was touched.

### Theorem 3.1 (gain/loss identity)

\[
\boxed{
\Phi(Q')-\Phi(Q)=|B_T|-|K_T|.}
\tag{3.2}
\]

In particular,

\[
\Phi(Q')<\Phi(Q)\quad\Longleftrightarrow\quad |K_T|>|B_T|.
\tag{3.3}
\]

#### Proof

The decompositions

\[
F(Q)=(F(Q)\cap F(Q'))\mathbin{\dot\cup}K_T,
\qquad
F(Q')=(F(Q)\cap F(Q'))\mathbin{\dot\cup}B_T
\]

are disjoint.  Subtract their cardinalities. \(\square\)

An old signed key which loses its frozen proof but acquires a different proof
remains in the intersection and is not killed.  Therefore proof destruction
is only a proposal mechanism; only complete reprobing determines \(K_T\) and
\(B_T\).

### Corollary 3.2 (weighted-global averaging)

For a finite packet family \(\mathcal L\), let \(\omega_T\ge0\).  If

\[
\sum_{T\in\mathcal L}\omega_T|K_T|
>
\sum_{T\in\mathcal L}\omega_T|B_T|,
\tag{3.4}
\]

then some \(T\in\mathcal L\) strictly lowers \(\Phi\).

#### Proof

Otherwise \(|K_T|\le|B_T|\) for every positively weighted packet, and the
reverse of (3.4) follows after summation. \(\square\)

Physical proof-incidence weights are a useful way to propose \(\omega\) or a
small target set, but incidence alone does not prove (3.4): touching a halo
need not destroy the failed literal, and a packet may create new failures.

## 4. Exact global certificate-incidence focus

Freeze one two-branch contradiction provenance for each \(f\in F(Q)\).  Let
\(P_f(Q)\) be the set of present `blue_remove` physical edges occurring in
the union of the two branch cores.  Repetition within a core or between the
two branches is discarded.  Define

\[
w_Q(e)=\bigl|\{f\in F(Q):e\in P_f(Q)\}\bigr|.
\tag{4.1}
\]

The implemented rule sorts present blue edges by \((-w_Q(e),e)\), retains
the first nine, enumerates every connected alternating physical
\(C_4,C_6,C_8\) containing at least one retained edge, filters by degree two
and complete lower/upper q1 support, and then recomputes the entire new
fixpoint and failure bank.  No Farkas coefficient, core-size weight, branch
multiplicity, or predicted packet gain enters (4.1).

For a packet with deleted edge set \(D_T\), two useful diagnostics are

\[
W_Q(T)=\sum_{e\in D_T}w_Q(e),
\qquad
H_Q(T)=\bigl|\{f:P_f(Q)\cap D_T\ne\varnothing\}\bigr|.
\tag{4.2}
\]

Neither is a descent certificate.

At \(Q_{30}\), the selected edge/weight pairs are

\[
\begin{gathered}
(60232,61192):8;\\
(41181,42189):7,\ (42169,42680):7,\ (42201,42232):7,\\
(42201,46233):7,\ (45261,46157):7;\\
(18558,26718):6,\ (22814,55578):6,\ (26718,27678):6.
\end{gathered}
\tag{4.3}
\]

### Theorem 4.1 (statewise failure of incidence monotonicity)

At the frozen \(Q_{30}\), the declared top-nine atlas contains 64 legal
packets.  Their exact outcomes are

\[
13\text{ improving},\quad16\text{ neutral},\quad30\text{ worsening},
\quad5\text{ ordinary unit contradictions}.
\tag{4.4}
\]

In particular, the alternating \(C_6\)

\[
\begin{aligned}
D_-&=\{(42169,42680),(42673,59025),(58521,58552)\},\\
A_-&=\{(42169,58552),(42673,42680),(58521,59025)\}
\end{aligned}
\tag{4.5}
\]

has \((W,H)=(7,7)\) and \(\Phi(Q^{T_-})=27\), whereas the alternating
\(C_4\)

\[
\begin{aligned}
D_+&=\{(42139,45211),(42201,46233)\},\\
A_+&=\{(42139,42201),(45211,46233)\}
\end{aligned}
\tag{4.6}
\]

has the same \((W,H)=(7,7)\) and \(\Phi(Q^{T_+})=34\).  Both preserve
degree two and complete lower/upper q1 support.

#### Proof

The declared atlas is the complete 64-packet output of the frozen generator
for connected radii-two-through-four circuits through its top-nine focus.
The generator computed each complete bank.  The pinned lightweight replay
checks input hashes, the two edge symmetric differences, factor structure,
q1-support ledgers, (4.1)--(4.2), and the stored outcome census.  The two
displayed packets have equal diagnostics and opposite score direction.
\(\square\)

Consequently the observed birth-free prefix cannot be promoted to a theorem
by summing old proof incidences.  A valid averaged theorem must establish
(3.4) using exact killed and born banks, or introduce a stronger dual which
charges replacement proofs and newly eligible failures.

## 5. What positivity alone does and does not prove

Let \(G_{\mathcal L}^{\rm uc}\) be the finite directed graph whose vertices
are q1 factors on which ordinary unit propagation reaches a noncontradictory
fixpoint, so \(\Phi\) is defined, under a declared legal packet relation.  Let
\(N^+_{\mathcal L,\mathrm{uc}}(Q)\) contain only successors whose complete
ordinary unit propagation has a noncontradictory fixpoint.  The desired
universal descent statement is exactly

\[
\tag{UD}
\forall Q\in V(G_{\mathcal L}^{\rm uc})\quad
\Phi(Q)>0\Longrightarrow
\exists Q'\in N^+_{\mathcal L,\mathrm{uc}}(Q):
\Phi(Q')<\Phi(Q).
\]

Equivalently, \(G_{\mathcal L}^{\rm uc}\) has no positive-score local
minimum.  Under (UD), every maximal strict-descent path ends at score zero
after at most its initial score.  Conversely, a positive local minimum
refutes (UD).

The weaker assertion that each undirected/reversible component merely
contains a score-zero state is not sufficient: a positive local minimum can
coexist with a zero state elsewhere in the same component.  Positivity of
the integer \(\Phi\) by itself supplies none of this graph geometry.  No
positive local minimum for the full physical trade graph is certified here,
so this is not a statewise physical no-go.  The statewise negative theorem
proved here is only Theorem 4.1: the implemented incidence weight is not
monotone.  The universal quantifier (UD) remains open.

For the implemented mechanism, (UD) specializes to the state-dependent
library \(\mathcal T_9(Q)\) of all generated connected
\(C_4,C_6,C_8\) packets through the nine edges selected by (4.1).  Even this
restricted universal statement is unproved; Theorem 4.1 only rules out
proving it from \((W,H)\) alone.

## 6. Eligibility/UP/Farkas halo

For a certificate \(\mathfrak c_v\), define its exact primitive halo
\(\mathcal H(\mathfrak c_v)\) to contain:

1. every physical decision edge in
   \(E_v,\Pi_v^0,\Pi_v^1,\Lambda_v^0,\Lambda_v^1\);
2. the complete provider list and load for each used q1 row;
3. the complete red/blue endpoint star for each used degree row;
4. every occurrence-labelled cycle collar and closure for each used motif;
5. a **complete closure certificate** for the full fixpoint: a derivation of
   every literal fixed by \(\sigma_Q\), followed by the residual slack and
   nonforcing check for every normalized row of \(\Sigma(Q,R)\), together
   with the complete row census; this proves both inclusions between the
   derived closure and the displayed stable assignment and hence proves that
   \(v\) is genuinely unassigned in the complete fixpoint;
6. every ordered forcing step, pre-step fixed value, residual slack/bound,
   and final contradictory row in both branch-UP transcripts, together with
   every row coefficient, right-hand side, and multiplier in the two derived
   Farkas packets.

A packet \(T\) **transports** \(\mathfrak c_v\) to
\(\mathfrak c_{v'}\) if there is an injective row/variable map taking all six
halo data itemwise to the new atlas, and each replayed closure/transcript row
is carried by a coefficient- and right-hand-side-preserving isomorphism onto
its **entire** target support.  The ordered residual forcing calculation at
every transcript step must replay exactly.  Any target term outside the image
must be explicitly certified to have coefficient zero.  In addition, the
target closure certificate must check every target row, including rows
outside the image.
Reusing the same multipliers then proves

\[
v'\in F(Q').
\tag{6.1}
\]

Geometric disjointness of packet edges from proof edges is not sufficient:
rethreading may change an occurrence collar or eligibility fixpoint remotely.
The itemwise atlas condition is the theorem-safe notion of halo inertia.

The global closure clause is essential.  Merely preserving the rows used in
the old propagation is not enough: non-fixation is a negative property, and
a newly changed row can force \(v'\) without appearing in the old
provenance.

### Lemma 6.1 (halo transport)

If \(T\) transports certificates for a set \(S\subseteq F(Q)\) injectively,
then

\[
\Phi(Q')\ge|S|.
\tag{6.2}
\]

#### Proof

The derivation half and stable-row half of item 5 prove that the transported
assignment is exactly the target full fixpoint, so eligibility is preserved.
Item 6 then replays each ordered forcing step and the final contradiction on
both branches.  Hence the target deterministic unit propagation contradicts
under each value, so each transported variable is a failed literal.  The
replayed Farkas combinations are an additional semantic check, not the reason
for algorithmic bank membership.  Injectivity makes them distinct.
\(\square\)

## 7. Necessary-and-sufficient finite local-minimum certificate

Fix a finite declared library \(\mathcal L(Q)\) of legal q1-support-complete
packets and let \(N=\Phi(Q)\).

### Theorem 7.1 (finite failed-literal alternative)

Exactly one of the following holds.

**Descent.** There exist \(T\in\mathcal L(Q)\) and a complete bank audit with

\[
\Phi(Q^T)<N.
\tag{7.1}
\]

**Local-minimum certificate.** For every \(T\in\mathcal L(Q)\), either

1. ordinary unit propagation on \(\Sigma(Q^T,R)\) contradicts; or
2. there exists a set \(W_T\) of \(N\) distinct eligible variables of
   \(Q^T\) such that

   \[
   \forall w\in W_T\ \forall\varepsilon\in\{0,1\}\ 
   \exists\Pi_{T,w}^{\varepsilon}
   \quad
   \Pi_{T,w}^{\varepsilon}
   \text{ is an exact ordered branch-UP transcript ending in contradiction},
   \tag{7.2}
   \]

   with an exact complete-fixpoint eligibility certificate for every \(w\).
   Each transcript may additionally carry the derived
   \(\Lambda_{T,w}^{\varepsilon}\ge0\) yielding \(0\le-1\), but that
   semantic certificate cannot replace \(\Pi_{T,w}^{\varepsilon}\).

In addition, the certificate must contain a completeness proof that every
packet satisfying the declared library definition appears in the quantified
list.

#### Proof

If (7.1) holds, neither clause for that \(T\) can supply \(N\) failed literals,
so the alternatives are disjoint.  If no descent exists, each unit-consistent
endpoint has \(\Phi(Q^T)\ge N\); choose any \(N\) members of its complete bank
and their certificates (2.5).  Conversely, exact eligibility plus the two
ordered contradiction transcripts in (7.2) prove
\(\Phi(Q^T)\ge N\) for every unit-consistent endpoint, while unit-contradictory
endpoints are already infeasible and are not lower-bank witnesses. \(\square\)

### Halo-compressed form

For each \(T\), it suffices to partition

\[
W_T=W_T^{\rm transported}\mathbin{\dot\cup}W_T^{\rm fresh}.
\]

Give injective halo maps, including the complete target closure check and
ordered two-branch transcript replay, for the transported part and explicit
eligibility plus two branch-UP transcripts for the fresh part.  Derived
Farkas packets are useful cross-checks.  A particularly efficient library
audit is:

1. enumerate and fully score every legal packet which changes at least one
   frozen halo datum;
2. for every omitted packet, prove itemwise preservation of all \(N\) frozen
   halos, giving \(W_T=F(Q)\).

This is a finite, proof-safe local-minimum certificate.  It proves nothing
about larger packets, another declared library, moving \(R\), or exact Hall
deficiency \(\Delta_R(Q)\).

## 8. Candidate-1 and candidate-2 calibration

The two alternate zero-unit-core endpoints independently exhibit the same
gap between ordinary unit propagation and failed-literal propagation.

| endpoint | motifs | rows | two-choice bank | unhit two-choice motifs | double failures |
|---|---:|---:|---:|---:|---:|
| candidate 1 | 2250 | 50864 | 979 | 516 | 93 |
| candidate 2 | 2251 | 50865 | 981 | 517 | 93 |

Every candidate variable in each bank was probed.  Both artifacts have zero
ordinary unit cores and exact status `BINARY_IMPLICATION_CONTRADICTION` in the
independent residual implication audit.  Hence the bank is not a peculiarity
of candidate 0.

Endpoint hashes:

```text
candidate 1: 7435b0f27e035e2eec87ec5afe47130fd2d08da3bcee70669a4189f4bb7d6dff
candidate 2: ce17d15a6474cf20108412a6b255a91b8bab7566a27bbedf75dad8eb1002d738
```

Complete-bank hashes:

```text
candidate 1: c77cdb309c47ba3ee14120004c4a6e9ec4b684b4e6bb87dea0a6dfddc9d0821f
candidate 2: 625b56c114c2c98d30bd7ea4dc882bc53abba62e609065e87793c6cd070c669f
```

## 9. Frozen global-incidence descent from FL73 through FL30

The first arrow below uses the twelve-edge focus of the smallest frozen
failed-literal core.  The remaining five arrows use (4.1)'s global top-nine
focus.  Thus the entire prefix is proof-directed, but only the suffix is an
instance of the global incidence rule.

### Theorem 9.1 (exact birth-free prefix)

Starting at the frozen \(Q_{73}\), apply the following packets in order:

\[
\begin{aligned}
D_{73}&=\{(6630,14694),(7526,15714),(13796,14820),(15713,15840)\},\\
A_{73}&=\{(6630,14820),(7526,14694),(13796,15840),(15713,15714)\};
\end{aligned}
\tag{9.1}
\]

\[
\begin{aligned}
D_{69}&=\{(37331,45459),(37333,45521),(45395,46355),(45397,46417)\},\\
A_{69}&=\{(37331,45521),(37333,45397),(45395,46417),(45459,46355)\};
\end{aligned}
\tag{9.2}
\]

\[
\begin{aligned}
D_{56}&=\{(35558,51940),(35564,51944),(51430,55462),(55466,55976)\},\\
A_{56}&=\{(35558,51430),(35564,51940),(51944,55976),(55462,55466)\};
\end{aligned}
\tag{9.3}
\]

\[
\begin{aligned}
D_{48}&=\{(41531,57907),(49723,49978),(57651,57658),(57914,59450)\},\\
A_{48}&=\{(41531,49723),(49978,57914),(57651,57907),(57658,59450)\};
\end{aligned}
\tag{9.4}
\]

\[
\begin{aligned}
D_{39}&=\{(49518,51502),(51562,57706),(57646,59690)\},\\
A_{39}&=\{(49518,51562),(51502,57646),(57706,59690)\};
\end{aligned}
\tag{9.5}
\]

\[
\begin{aligned}
D_{34}&=\{(42139,42201),(45211,45465),(45459,46481),(46227,46233)\},\\
A_{34}&=\{(42139,45211),(42201,46233),(45459,45465),(46227,46481)\}.
\end{aligned}
\tag{9.6}
\]

The six symmetric differences are respectively
\(C_8,C_8,C_8,C_8,C_6,C_8\).  Exact replay gives

| state | \(\Phi\) | probe bank | components | short occurrences | lower/upper q1 holes |
|---|---:|---:|---:|---:|---:|
| \(Q_{73}\) | 73 | 970 | 4 | 2240 | 0/0 |
| \(Q_{69}\) | 69 | 970 | 3 | 2236 | 0/0 |
| \(Q_{56}\) | 56 | 969 | 4 | 2235 | 0/0 |
| \(Q_{48}\) | 48 | 968 | 4 | 2233 | 0/0 |
| \(Q_{39}\) | 39 | 956 | 3 | 2235 | 0/0 |
| \(Q_{34}\) | 34 | 960 | 3 | 2235 | 0/0 |
| \(Q_{30}\) | 30 | 958 | 3 | 2236 | 0/0 |

On signed failure tokens, the six pairs \((|K_T|,|B_T|)\) are

\[
(4,0),(13,0),(8,0),(9,0),(5,0),(4,0).
\tag{9.7}
\]

#### Proof

The independent chain audit starts from each frozen endpoint, applies the
displayed deletion/addition sets, and checks equality with the next frozen
edge set.  It verifies that every symmetric difference is one connected
alternating cycle, every state is a simple degree-two spanning factor, and
all 11,440 targets on each q1 shore retain positive load.  It independently
reconstructs the component and short-occurrence counts, reads each complete
probe bank, and compares signed failure keys.  The bank differences are
exactly (9.7), so Theorem 3.1 gives every displayed score. \(\square\)

The endpoint and bank hashes are:

| state | endpoint SHA-256 | complete-bank SHA-256 |
|---|---|---|
| 73 | `fa7d6edce1a71012d317220a97e0cf8900dd14d385087ea3a6d920a64d16e513` | `d03193607795d42865e16277888c4ea0c3c025499fcd78c966077a131cde7c47` |
| 69 | `60e8922b557465ded1640f93d0076ddbdd7ee42a033871f443b1b61a0660654b` | `22d28e7059f5e6e35a98c8b420f8b8267d190c7beef942217c174f09c08aebbe` |
| 56 | `8ee32b82024879e68367aa28f5dea60380ba603d2cbcbc939052b8ba49c5ea50` | `9665260222cd47d33f67e80cbec6c6130afb0fc6441237c9bfe4261f05e808a3` |
| 48 | `5502b394772167f50058e6b38a37640e1828e09e67ce0624521d7dff7b333287` | `433576913753b8b7d23cfffc30be2ed86f44e84f1a1e1a4fe54ce890db1a4107` |
| 39 | `db809954e287b1468dcd75b46ba2cd2f3fde4618c427d14c377dbedd381ca1be` | `da9631d4c7ce9846b1e3e96317e035fc1e7389979788a4c79ff65f699948ba56` |
| 34 | `bd872b21b98a98a7cbda6b94823b39d2ba5b77dea5d21a9db2a174f6fdd96717` | `51b3709fc5a93ee9afcf5f3326736e20897b6c99b236ac2dfe1823e3f7bd4986` |
| 30 | `2c44459ff9a7b005915a9cbb9235970fc7928790d71023ccbb2262ec593dcdf0` | `7cd1afabe031924d8b50d4e10bf47793df60991b1f743d28ded4aa109cd1be03` |

The six source-report hashes, in chronological order, are

```text
997769857307886f798015bdcd9d943ab4eac3404913a0907bb7e0bea859d0d9
9caaf0695c032d6f65662b33eb79c8d0cabf865e674f12bf2509a47630f05ccb
9fb811da32fbc31807efdf29603956513a92a22d12c42af89234e5bfc7c9fdf9
fc1e54453ae486f83d1ad80e8924226b447f337bb6e38f06fd887df7b3fa824f
61898e9c231e7462221f09bb2c3e353fc880829e25e6ab341a8b6df442ce7d95
e8770e4b02ff855bc39e86f2094b04e3696e6980955dc1942e561623a69a2026
```

## 10. Exact FL30-to-FL27 calibration

The FL30 endpoint has:

\[
2236\text{ motifs},\quad505\text{ unhit two-choice motifs},
\quad958\text{ fully probed candidates},\quad\Phi=30.
\]

The declared search library consists of every connected alternating
q1-support-complete packet of radii \(2,3,4\) through the nine most frequent
physical proof edges in the frozen FL30 bank.  Exactly 64 packets were
generated and all 64 were scored.  Their bank histogram is

\[
27^9,\ 29^4,\ 30^{16},\ 31^8,\ 34^{15},\ 35^1,
\ 37^2,\ 38^3,\ 39^1,
\]

plus five endpoints with an ordinary unit contradiction.

One best packet deletes

\[
(42169,42680),\quad(42673,59025),\quad(58521,58552)
\]

and adds

\[
(42169,58552),\quad(42673,42680),\quad(58521,59025).
\]

It is an alternating \(C_6\), leaves zero q1 holes, changes the component
count \(3\to2\), and changes the short-occurrence count
\(2236\to2234\).  The complete new bank has 959 candidates and 27 double
failures.

Comparing signed physical keys gives

\[
|F(Q_{30})\cap F(Q_{27})|=27,
\qquad |K_T|=3,
\qquad |B_T|=0.
\]

The three lost failed literals are

```text
blue_remove (38105,40137)
blue_remove (50394,54488)
blue_remove (54481,54488)
```

so Theorem 3.1 yields the exact descent \(30-3+0=27\).  None of these three
literal edges is itself in the \(C_6\); the packet acts through their nonlocal
proof/eligibility halos.

Frozen hashes:

```text
FL30 endpoint: 2c44459ff9a7b005915a9cbb9235970fc7928790d71023ccbb2262ec593dcdf0
FL30 bank:     7cd1afabe031924d8b50d4e10bf47793df60991b1f743d28ded4aa109cd1be03
packet atlas:  972be30ea39f78ff48adc31cf1f5c82e40cc78bfe1f0692cee9f3e0946ba0765
FL27 endpoint: ded151910d332d6e77c4c6fc3bb10e6ada6f4046b25054178f6d21742b2c4491
FL27 bank:     2e6914c5c748ae80c08997a8eb17bd2ffaa8d1efe51b966f019ffebb1f6c1eba
```

## 11. Scope and next exact gate

What is proved:

- failed-literal packet change obeys the exact gain/loss identity;
- weighted aggregate loss exceeding creation forces a descent;
- proof-incidence weight alone does not force descent;
- Theorem 7.1 gives a necessary-and-sufficient finite local-minimum
  certificate with exact complete-fixpoint eligibility and two ordered
  branch-UP contradiction transcripts per retained failure; derived Farkas
  packets are cross-checks;
- the declared FL30 library contains a literal descent to FL27 with no new
  failed literal.

What is not proved:

- that every positive-bank endpoint has a lowering packet;
- that \(\Phi=0\) implies overlay feasibility or \(\Delta_R=0\);
- that the top-nine library is sufficient beyond FL30;
- any obstruction to larger/nonconnected packets or a moving resident.

The labels FL73, ..., FL30, FL27 refer to this frozen ancestry and its
declared banks.  They are not a claim about the live minimum after concurrent
packet lanes; the purpose of the prefix is to certify the theorem and the
mechanism exactly.

At a future positive terminal state, the theorem-safe deliverable is not a
claim that the heuristic is stuck.  It is the finite certificate of Theorem
7.1: a complete library enumeration, transported halos for inert packets, and
explicit replacement eligibility/transcript packets for every halo-changing
packet.  No such first-stall certificate is asserted here: FL30 has thirteen
lowering packets in its declared atlas, including the frozen FL27 endpoint.

## 12. Lightweight audits

Frozen \(Q_{73}\to Q_{30}\) chain replay:

```text
scratch/audit_k16_failedlit73_to30_weighted_global_chain_20260729.py
SHA-256 9b40d0e225a4c21503542bdb4b8b6ef382d62413de060d5a509a5d300ddc20fc

scratch/k16_failedlit73_to30_weighted_global_chain_20260729.audit.json
SHA-256 257dfa7e4139d743c61f94a45ffe2e1a0c2b9e5982d6987422f74ade538331ef
status PASS_EXACT_FROZEN_CHAIN
```

FL30 incidence nonmonotonicity replay:

```text
scratch/audit_k16_fl30_packet_weight_nonmonotonicity_20260729.py
SHA-256 7d4ba3759bd3a2c50b3f4cc32840106bcbf721db0df40f877cf855e2f6ddbc1f

scratch/k16_fl30_packet_weight_nonmonotonicity_20260729.audit.json
SHA-256 ab912bd87879bce0b6489c1716aa94f8b0074be538716b29c0fc6c667fb485a7
status PASS
```

Candidate-1/candidate-2 and FL30-to-FL27 replay:

```text
scratch/audit_k16_candidate12_fl30_halo_transition_20260729.py
SHA-256 b89b569311494c8c7d8125f4288bf58505e51435ea8356d858bad98eea5353ed

scratch/k16_candidate12_fl30_halo_transition_20260729.audit.json
SHA-256 df8fbcdeb7b8bc542a8918b50d0709be76d8102abe7cd8b1dfecc9d867f0de62
status PASS
```

All three audits are read-only exact artifact replays.  The chain audit
reconstructs the structural and bank-difference ledgers from frozen banks;
the incidence audit verifies structures, weights, support ledgers, hashes,
and the stored full-bank outcome census rather than rerunning all branch
probes.  They launch no SAT, CP-SAT, Kissat, H100, or exhaustive local search.
