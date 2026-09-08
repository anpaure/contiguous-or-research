# K16 singleton-packet packing and small-trade scope audit

Date: 2026-07-29  
Lane: K  
Status: exact solver-free lower bound in three fixed overlays; adversarial scope audit of the local `C6` claims

## 1. Verdict

Fix the audited `resume1` resident factor (R).  For each of the three named
q1-complete zero-unit-detector endpoints (Q_0,Q_1,Q_2), let
(Delta_R(Q_i)) be the minimum number of **inherited** short-residence
occurrences left unhit by any degree-two, lower-q1-cover-preserving and
upper-q1-cover-preserving choice inside the fixed overlay (R\cup Q_i).
Then

\[
\boxed{\Delta_R(Q_i)\ge 15\qquad(i=0,1,2).}
\tag{1.1}
\]

The proof is solver-free and stronger than the earlier common one-motif and
two-motif packets.  Candidates 1 and 2 each contain fourteen distinct
inherited occurrences whose motif row is individually incompatible with the
hard degree-plus-both-q1 system.  Candidate 0 contains thirteen of those
transported singleton locks and its separate motif-82 singleton lock.  All
three also contain the same two-motif serial packet, disjoint from the
fourteen singleton occurrences, which forces one additional hole.

Thus the zero unit-core detector was not close to feasibility: it merely
failed to expose a packet packing already of size fifteen.

The exact iterative potential remains the full interaction-hypergraph
transversal

\[
\Delta_R(Q)=\tau(\mathscr C_R(Q)).
\tag{1.2}
\]

A theorem-safe computable lower potential is the maximum total deficit of a
motif-disjoint family of independently certified affine or failed-literal
packets.  Counts such as `93 -> 87` failed literals are useful search scores,
but are not values of (1.2) and do not by themselves prove strict descent.

## 2. Fixed-overlay system

Put

\[
B=Q\setminus R,\qquad A=R\setminus Q.
\]

For (e\in B), let (b_e=1) mean that (e) is deleted from (Q).  For
(f\in A), let (a_f=1) mean that (f) is inserted.  The hard system
(\mathcal H_R(Q)) consists of

\[
a_f,b_e\in\{0,1\},
\tag{2.1}
\]

the exact endpoint equations

\[
\sum_{f\in A(v)}a_f=\sum_{e\in B(v)}b_e
\quad(v\text{ a middle vertex}),
\tag{2.2}
\]

and, for every represented lower or upper q1 colour (c),

\[
\sum_{e\in B_c}b_e-\sum_{f\in A_c}a_f\le \mu_Q(c)-1.
\tag{2.3}
\]

The zero vector satisfies this hard system.  If (M) is an inherited
short-run occurrence with physical collar (C_M), its row is

\[
\sum_{e\in C_M\cap B}b_e\ge1.
\tag{2.4}
\]

An occurrence is a **singleton lock** when
(\mathcal H_R(Q)+(2.4)) is infeasible.  Such an occurrence survives under
every hard-feasible overlay assignment.

More generally, if (P_1,\ldots,P_s) are infeasible motif packets with
pairwise disjoint occurrence sets, then every hard-feasible assignment leaves
at least one occurrence unhit in every (P_j).  Hence

\[
\Delta_R(Q)\ge s.
\tag{2.5}
\]

This is the elementary packet-packing lower bound.  It does not require that
the displayed packets exhaust all minimal circuits.

## 3. Fourteen independently replayed singleton locks

The complete failed-literal banks for candidates 1 and 2 were used only to
locate candidate occurrences.  Every claimed singleton was then replayed
from scratch against **only** the exact hard rows (2.1)--(2.3) and its own
single motif row (2.4).  For a selected physical probe (x), both branches
(x=0) and (x=1) end in exact signed-cardinality contradictions.  The
union of the two branch provenances contains that one motif row and no other
motif row.  Because the hard base has the all-zero witness, the motif support
is inclusion-minimal.

The fourteen common physical singleton keys for candidates 1 and 2 are:

| coordinate | length | physical collar |
|---:|---:|---|
| 0 | 2 | `52747-52750, 52747-52777, 52777-52792` |
| 1 | 2 | `34397-34398, 34398-50270, 50270-52316` |
| 1 | 2 | `43118-43370, 43118-59500, 43370-44392` |
| 2 | 1 | `45397-45425, 45397-46417` |
| 3 | 2 | `41395-41401, 41401-42409, 42409-46497` |
| 4 | 2 | `47491-47505, 47505-47568, 47556-47568` |
| 4 | 3 | `43132-43256, 43132-51324, 43256-43496, 51324-51564` |
| 5 | 2 | `39100-40116, 39100-47260, 40085-40116` |
| 6 | 2 | `17127-21095, 17127-25255, 21039-21095` |
| 9 | 2 | `41551-41615, 41551-57423, 41615-45199` |
| 9 | 2 | `56472-56968, 56588-56844, 56844-56968` |
| 11 | 2 | `49881-51921, 51921-56016, 53972-56016` |
| 11 | 2 | `62050-64034, 62514-63538, 63538-64034` |
| 13 | 2 | `51595-59531, 53451-57547, 57547-59531` |

Candidate 0 contains thirteen of these.  The absent key is the coordinate-3
collar

\[
\{41395\!-!41401,41401\!-!42409,42409\!-!46497\}.
\]

In its place candidate 0 has the independently Farkas-certified motif 82,

\[
\{34233\!-!42409,38307\!-!46497,42409\!-!46497\},
\tag{3.1}
\]

at coordinate 13 and length two.  Every removable collar candidate in
(3.1) is hard-forbidden.

One of the fourteen common locks is especially transparent.  For

\[
C=\{62050\!-!64034,62514\!-!63538,63538\!-!64034\},
\]

put

\[
\begin{array}{lll}
x=b_{63538,64034},&y=b_{62050,64034},&z=b_{62514,63538},\\
a=a_{63526,64546},&b=b_{63526,63750},&c=a_{61486,63526},\\
d=b_{59438,63526},&p=a_{61554,63538},&q=a_{48178,63538}.
\end{array}
\]

The four hard rows

\[
x-a\le0,\quad b\le0,\quad a+c-b-d\le0,\quad d-c\le0
\]

sum to (x\le0).  The motif row and four further hard rows

\[
-x-y-z\le-1,\quad y\le0,\quad z-p\le0,\quad z-q\le0,
\quad p+q-z-x\le0
\]

sum to (-2x\le-1).  Twice the first sum plus the second gives
(0\le-1).  This certificate works over the reals and is shared verbatim by
all three endpoints.

## 4. The fifteenth forced hole

All three endpoints also inherit the disjoint two-motif packet

\[
\begin{aligned}
A={}&\{7526\!-!7782,7526\!-!15714,15466\!-!15714\},\\
B={}&\{47458\!-!63810,48210\!-!63570,63570\!-!63810\}.
\end{aligned}
\tag{4.1}
\]

Exact hard-row sums give, with

\[
H_1=b_{15466,15714}+b_{7526,15714},\qquad
H_2=b_{47458,63810}+b_{63570,63810},
\]

and suitable nonnegative binary variables (s,h,e),

\[
H_1+s\le h,\qquad H_2+e\le s,\qquad h\le1.
\tag{4.2}
\]

Hitting both occurrences requires (H_1,H_2\ge1), contradicting

\[
H_1+H_2+e\le h\le1.
\tag{4.3}
\]

The two occurrence labels in (4.1) are disjoint from all fourteen singleton
locks listed in Section 3.  Applying (2.5) to the fourteen singleton packets
and the packet ({A,B}) proves (1.1).

## 5. What costs the second unit at radius 98

The scalar palette-weighted transversal (98) solves only the internal
motif-hitting choice.  It does not solve the simultaneous endpoint-coloured
completion problem.  For a fixed source cut (D), let

\[
\mathcal B_R(D)=
\{S:\deg_S(v)=\deg_D(v)\text{ for every endpoint }v\}
\]

be the allowed seam (b)-factors, and let (L_D,U_D) be the lower and upper
q1 rows whose complete source-provider sets are deleted by (D).  Define

\[
\delta_{LU}(D)=
\min_{S\in\mathcal B_R(D)}
\bigl(|L_D\setminus\lambda(S)|+|U_D\setminus\upsilon(S)|\bigr).
\tag{5.1}
\]

Then a cut is full-hard feasible exactly when (\delta_{LU}(D)=0), together
with the separately imposed top/residence conditions.  The exact global
invariant is therefore the endpoint-conditioned coloured-(b)-factor rank,
not either palette rank separately.  In the certified 262-option internal
radius-98 product, every option has positive joint deficiency even though
degree alone and either palette separately can be feasible.  This is the
second surcharge.

For iterative re-centering, the exact fixed-overlay potential is (1.2).  A
practical proof-safe lower approximation is

\[
\Pi_R(Q)=
\max\left\{
\sum_j d(P_j):
P_j\text{ are motif-disjoint certified packets}
\right\},
\tag{5.2}
\]

where (d(P_j)) is the packet's certified minimum number of failed motif
rows.  Always

\[
\Pi_R(Q)\le\Delta_R(Q).
\tag{5.3}
\]

A trade that leaves every motif collar and every hard row used by a packet
unchanged transports that packet and its deficit.  Thus (5.2) gives a local
support criterion for genuine progress.  Strict descent of the exact
potential requires both:

1. an old-state packet packing giving (\Delta_R(Q)\ge p); and
2. a new-state hard-feasible assignment leaving at most (p-1) inherited
   occurrences unhit.

Merely lowering a failed-literal count or a greedy core count supplies no
such upper witness.

## 6. Adversarial audit of the local `C6` claims

### 6.1 Support-preserving A/B census

The script
`audit_k16_candidate1_ab_trade_failed_literal_potential_20260729.py`
enumerates all connected alternating support-two and support-three exchanges
that delete a closure edge of (A) or (B).  At support at most three there
is no nontrivial disconnected exchange: every nonempty balanced component
uses at least two deleted edges.  The alternating-walk generator therefore
covers the claimed library.  Every retained candidate is independently
checked to be a spanning degree-two factor.

The exact counts are

\[
\begin{array}{c|cc|cc}
 &A,C_4&A,C_6&B,C_4&B,C_6\\ \hline
\text{raw}&33&1134&33&1131\\
\text{both-q1-support preserving}&0&4&1&7.
\end{array}
\]

After deduplication there are twelve candidates.  The best displayed trade
is

\[
\begin{aligned}
D={}&\{47395\!-!55587,47458\!-!63810,55619\!-!63747\},\\
S={}&\{47395\!-!47458,55587\!-!55619,63747\!-!63810\}.
\end{aligned}
\tag{6.1}
\]

It destroys (B), preserves lower and upper q1 **support**, changes the
complete two-choice failed-literal detector count from (93) to (87), and
changes the number of current short occurrences from (2250) to (2251).
It is not token-multiset preserving, it leaves the common singleton lock
(C) intact, and no exact decrease of (Delta_R) follows.

An independently replayed three-trade chain has detector scores

\[
93\longrightarrow87\longrightarrow84\longrightarrow82,
\tag{6.2}
\]

while its current short-occurrence counts are

\[
2250\longrightarrow2251\longrightarrow2252\longrightarrow2253.
\tag{6.3}
\]

Every prefix is spanning degree two and has zero lower/upper q1 support
holes.  Again, (6.2) is a search-direction certificate, not a Lyapunov
theorem and not a feasibility certificate.

### 6.2 Strict-token connected `C6` census

For three deleted edges with exact lower- and upper-token multisets, pair the
three old lower tokens with the three old upper tokens.  A token pair
determines at most one physical Johnson edge.  After cancelling fixed pairs,
a genuine connected simple six-cycle can only use a three-cycle of the upper
tokens.  Enumerating both cyclic orientations for every target closure or
affine-support edge is therefore complete for the stated simple connected
strict-token `C6` library.

Exactly two candidates occur.  Both delete only an affine-support edge,
neither deletes the common collar (C), and their failed-literal detector
counts are respectively (93) and (90).  Therefore:

\[
\boxed{\text{no connected strict-token }C_6
\text{ through the named }A/B/C\text{ packet halo breaks }C.}
\tag{6.4}
\]

This is deliberately scoped.  It does not cover non-token-exact support
trades, disconnected unions, remote routers, `C8` or larger circuits, or a
change of resident factor.  Indeed a strict-token connected `C8` in the
same local atlas can delete a closure edge of (C); it lowers the detector
count only to (89), so it still does not certify exact descent or
feasibility.

## 7. Frozen evidence and hashes

Primary independent singleton-packing replay:

- `scratch/audit_k16_three_zero_endpoints_singleton_packet_packing_20260729.py`  
  SHA-256 `d6d41f761c413bea4fb5a5a76e203fe9e79bb5dc22e8216f3bbe9c2fc1fe4345`;
- `scratch/k16_three_zero_endpoints_singleton_packet_packing_20260729.audit.json`  
  SHA-256 `a13baa6ca351861959264381eb6a286fb58d9bf79cadeabd00b738ec144db70c`,  
  payload SHA-256 `225574bab572fbbb961b9464de9e28bd85a2336685307715104bf9f94a542988`.

The frozen endpoint hashes are

\[
\begin{array}{c|c}
Q_0&\texttt{6f614ae41d1264121acc7cfb1b3303f3bb93532d57aeac1d0153e3f344a73f53}\\
Q_1&\texttt{7435b0f27e035e2eec87ec5afe47130fd2d08da3bcee70669a4189f4bb7d6dff}\\
Q_2&\texttt{ce17d15a6474cf20108412a6b255a91b8bab7566a27bbedf75dad8eb1002d738}\\
R&\texttt{d28491b708d5a83e8abcde20fda8ad523cd58f9c662f46ae2d9c2507ba73e951}.
\end{array}
\]

Small-trade audits:

- A/B support-preserving census script/output:  
  `98ae7ff92419a019fa79e2652720b856764a25e5f0469656d27768ae4c7f6fc9`,  
  `439d387c189b15bb0a3e99090bb9a4de4e74b6ca3e2d53b487b8185a54c32d3c`;
- three-trade replay script/output:  
  `7ddb8f9de2f6fd1da0382adebd6c0a7a6c0d8ead8f8ecc7312651a10a527fbe3`,  
  `3293274746b449986d16c7034841bac390796db905c2dfb99d3bb48e55128d03`;
- strict-token `C6` enumeration script/output:  
  `c7ab191f25a268757ddae36a61001e672a39a2ecee3acd842b26bd084ea7206b`,  
  `1d72c952e2be52ae81470622225549b49b0dc00d9c7dc4a83de8b35fcbf3cc3b`;
- strict-token `C6` failed-literal audit script/output:  
  `55789efd1f85460b3637204b922b607e4e4ad7fcf1b1e18eb5b0e29c396af402`,  
  `6eeef48ac2a305a91c66f0ff54bb119dc0e7a112826d13a7d068c2fd332662b1`.

## 8. Sharp boundary

What is proved:

1. the three named zero-detector endpoints satisfy the fixed-overlay lower
   bound (Delta_R\ge15);
2. the second radius-98 surcharge is a joint endpoint-conditioned
   lower/upper palette defect, not a scalar motif-transversal defect;
3. the named connected strict-token `C6` halo cannot remove the common
   singleton packet;
4. a non-token-exact `C6` chain can lower a complete failed-literal working
   score while preserving q1 support.

What is not proved:

1. equality in (Delta_R\ge15);
2. monotonicity of the failed-literal score under arbitrary trades;
3. descent of (Delta_R) along the displayed `C6` chain;
4. absence of a remote, larger, non-token-exact, or moving-resident repair;
5. absence of newly created residence occurrences after a materialized
   overlay assignment.

The mathematically correct descent target is therefore a trade that destroys
or alters the row halo of a certified packet **and** comes with a matching
new-state upper witness for the exact inherited-hole potential.  Detector
reduction alone is insufficient.
