# K16 H2 non-provider ejection: closure, exclusive supply, and the exact two-cell no-go

Date: 2026-07-30  
Lane: K  
Status: proved for the frozen H2 word and independently replayed

## 1. Exact result and scope

Let $W$ be

    scratch/k16_ejection_lns_h2_p110_20260730.word

It has length $12873$, contains only nonzero $16$-bit masks, and has SHA-256

    5234b77101ac1f22ec1802b4e1f5eccb6f0fc6f540efff9bbd0dc92da8c09fe7.

Its exact hole set is

\[
A=0x4879,\qquad B=0x6879=A\mathbin\vee 0x2000.
\tag{1.1}
\]

This note proves:

1. an exact one-cell completion theorem using holes and all targets whose
   witnesses are exclusive to the edited position;
2. an exact at-most-three-form normal form and closure CNF for a fixed
   two-position support;
3. a containment/exclusive-supply essentiality cut, generalizing the earlier
   $p668$ reset argument;
4. an exact finite corridor atlas for the branch in which neither endpoint
   individually supplies $A$ or $B$; and
5. a complete no-go for that branch.

The finite conclusion is:

> **Frozen H2 two-edit theorem.** Every universal word obtained from $W$ by
> changing at most two positions has an endpoint whose final value, applied
> alone to $W$, supplies $A$ or $B$.

The exact provider-first result artifact separately exhausts every such first
move whose intermediate word has at most seven holes and finds no completing
second edit. Therefore every hypothetical two-edit completion of $W$, if one
exists, has a provider-first orientation whose intermediate word has at least
eight holes.

The last implication is logically exact, but the provider-sweep artifact does
not freeze the executed binary hash; Section 9 records that provenance caveat.
The independently replayed non-provider theorem is hash-closed.

This result does not exclude the remaining high-debt provider branch, three or
more edits, insertions/deletions, or another length-$12873$ word. The global
bracket remains

\[
12873\le \nu(16)\le12874.
\tag{1.2}
\]

## 2. Witnesses and exclusive supply

For a word $V=(v_0,\ldots,v_{n-1})$ and an interval $I=[i,j]$, write

\[
\Omega_V(I)=\bigvee_{t=i}^{j}v_t.
\]

An interval with $\Omega_V(I)=T$ is a $T$-witness. For a set of positions
$S$, define

\[
\rho^V_S(T)=
\#\{I:\Omega_V(I)=T,\ I\cap S=\varnothing\},
\qquad
\mathcal K_V(S)=\{T\ne0:\rho^V_S(T)=0\}.
\tag{2.1}
\]

Thus $\mathcal K_V(S)$ contains the holes of $V$ and every covered target all
of whose witnesses meet $S$. The latter are the exclusive-supply targets
that are missed if one reasons from the hole set alone.

Fix a position $q$ and a target $T$. Delete $v_q$, then extend left and right
from $q$ through the maximal consecutive blocks of fixed letters that are
submasks of $T$. Let their total OR and residual requirement be

\[
c^V_q(T),\qquad
r^V_q(T)=T\setminus c^V_q(T)
         =T\mathbin\&\neg c^V_q(T).
\tag{2.2}
\]

All shorter $q$-containing $T$-contexts are contained in this one maximal
context.

### Lemma 2.1 (one-cell provider interval)

After replacing $v_q$ by a nonzero mask $y$, a $q$-containing $T$-witness
exists if and only if

\[
r^V_q(T)\subseteq y\subseteq T.
\tag{2.3}
\]

#### Proof

Every letter in a $T$-witness is a submask of $T$, so $y\subseteq T$. No
fixed context can supply a bit of $r^V_q(T)$, so
$r^V_q(T)\subseteq y$. Conversely, the entire maximal context together with
such a $y$ has OR exactly $T$. This is a literal interval. ∎

### Theorem 2.2 (exact one-cell completion interval)

Put

\[
\mathcal S_q(V)=\mathcal K_V(\{q\}),\qquad
L_q(V)=\bigvee_{T\in\mathcal S_q(V)}r^V_q(T),\qquad
U_q(V)=\bigcap_{T\in\mathcal S_q(V)}T.
\tag{2.4}
\]

Use $\bigvee\varnothing=0$ and
$\bigcap\varnothing=0xffff$. Then $V$ has a universal completion by changing
only position $q$ if and only if

\[
U_q(V)\ne0,\qquad L_q(V)\subseteq U_q(V).
\tag{2.5}
\]

When (2.5) holds, every working value and only those values lie in the
nonzero part of the Boolean interval

\[
[L_q(V),U_q(V)]
=\{y:L_q(V)\subseteq y\subseteq U_q(V)\}.
\tag{2.6}
\]

In particular, the canonical largest value $y=U_q(V)$ works.

#### Proof

Every target outside $\mathcal S_q(V)$ retains a witness avoiding $q$.
Every target in $\mathcal S_q(V)$ must be resupplied through $q$. Applying
Lemma 2.1 simultaneously gives precisely the lower bound $L_q(V)$ and upper
bound $U_q(V)$. ∎

This is stronger than intersecting the current holes: it also preserves every
covered target whose entire supply passes through $q$.

## 3. Temporary-debt anchors

After a raw first edit $W^{a\leftarrow x}$, a target can be newly lost only
if all of its source witnesses meet $a$. Define

\[
\mathcal E_W(a)=\{T:\rho^W_{\{a\}}(T)=0\}.
\tag{3.1}
\]

Suppose the first edit supplies neither hole in (1.1), and let $D(a,x)$ be
its collateral debt set. If one further edit completes the word, its value
must be a submask of every current hole. Since $A\subset B$,

\[
A\cap\bigcap_{T\in D(a,x)}T\ne\varnothing.
\tag{3.2}
\]

Equivalently, some one of the seven coordinates of $A$ belongs to every
temporary debt. This gives seven exact anchor classes.

By Lemma 2.1, the exact one-cell provider domain for $T$ at $a$ is

\[
\mathcal A_a(T)=[r^W_a(T),T]\setminus\{0\}.
\]

For a chosen anchor $e\in A$, the raw non-provider values that eject no
$e$-omitting target lie in

\[
\left(
\bigcap_{\substack{T\in\mathcal E_W(a)\\ e\notin T}}
\mathcal A_a(T)
\right)
\setminus
\bigl(\mathcal A_a(A)\cup\mathcal A_a(B)\bigr).
\tag{3.3}
\]

This is exact for the intermediate nonempty-intersection screen. It is not a
completion theorem: for each proposed last position $q$, Theorem 2.2 must
also include covered targets whose witnesses are all $q$-dependent.

Consequently an exact non-provider-first enumeration never needs to scan
$65535$ last values. For each raw first edit and each $q$, it computes the
single interval (2.6). Either that interval is empty, giving a solver-free
certificate, or all possible last values are explicitly known.

## 4. Three undominated forms on a two-cell support

Fix $S=\{a,b\}$ with $a<b$. An interval meeting $S$ has one of the types

\[
J\in\{\{a\},\{b\},\{a,b\}\}.
\tag{4.1}
\]

For a target $T$ and type $J$, take the unique maximal fixed context obtained
by extending through consecutive fixed letters that are submasks of $T$. For
$J=\{a,b\}$, the whole bridge $a<i<b$ is forced; the form is invalid if a
bridge letter is not a submask of $T$. Let the maximal fixed OR be
$C^S_T(J)$.

### Lemma 4.1 (maximal-context dominance)

A $T$-witness of type $J$ exists after assigning values $x_a,x_b$ if and
only if

\[
C^S_T(J)\vee\bigvee_{p\in J}x_p=T.
\tag{4.2}
\]

#### Proof

Suffix ORs and prefix ORs adjacent to a variable cell form inclusion chains.
Every smaller $T$-compatible context is contained in the maximal one. If a
smaller context reaches $T$ with the variable values, enlarging it inside
$T$ still reaches $T$. The converse uses the literal maximal interval. ∎

### Theorem 4.2 (two-cell form section)

A substitution supported on $S$ is universal if and only if, for every
$T\in\mathcal K_W(S)$, at least one valid type $J$ satisfies (4.2).

#### Proof

Targets outside $\mathcal K_W(S)$ retain source witnesses avoiding both
positions. Every target inside it must use one of the three types, and
Lemma 4.1 is exact for each type. ∎

## 5. Closure and the exact projected CNF

Choose one form $f_T=(T,J_T,C_T)$ for each residual target and put

\[
Z_p=\bigcap_{T:p\in J_T}T,
\tag{5.1}
\]

with $Z_p=0xffff$ if no chosen form uses $p$. The section is realizable if
and only if $Z_a,Z_b\ne0$ and, for every selected form,

\[
T\setminus C_T
\subseteq
\bigvee_{p\in J_T} Z_p.
\tag{5.2}
\]

When these conditions hold, $x_p=Z_p$ is a canonical realization. Therefore
the complete projected failures are:

1. an empty intersection of selected target masks at one cell; or
2. a coordinate required by a form but omitted from every selected cell
   available to that form.

An exact form-selector CNF uses at most $3|\mathcal K_W(S)|$ form bits and
$32$ cell-availability bits. It consists of target menus, availability
rows, cell-nonzero clauses, and coordinate-cover clauses.

For an ordered chronology whose first value must remain a literal
non-provider, jointly closing both cells can be unsound: enlargement can turn
the first value into a provider. Keep its $16$ bits raw and closure-normalize
only the last cell. If $H$ is a source hole, the exact clause saying that raw
value $x$ at $a$ does not supply $H$ is

\[
\left(\bigvee_{e\notin H}x_e\right)
\vee
\left(\bigvee_{e\in H\setminus c^W_a(H)}\neg x_e\right).
\tag{5.3}
\]

Conjoin (5.3) for $A$ and $B$.

## 6. Containment/exclusive-supply essentiality

The exact provider atlas proves that $W$ has no one-edit completion. Hence
both endpoints of any at-most-two-edit completion are essential; allowing a
value to equal its incumbent in the CNF does not enlarge the satisfying set.

Consider resetting endpoint $a$ to its incumbent value $w_a$. A selected
$a$-using form $f=(T,J,C)$ survives the reset exactly when

\[
w_a\subseteq T
\quad\text{and}\quad
T\setminus(C\vee w_a)
\subseteq
\bigvee_{p\in J\setminus\{a\}}x_p.
\tag{6.1}
\]

If every selected $a$-using form survived, all other selected forms and all
source witnesses avoiding $S$ would also survive. That would give a one-edit
completion, a contradiction. Therefore every two-cell section must select
an $a$-using form with either

\[
w_a\not\subseteq T,
\tag{6.2}
\]

or

\[
T\setminus(C\vee w_a)
\not\subseteq
\bigvee_{p\in J\setminus\{a\}}x_p.
\tag{6.3}
\]

For $J=\{a\}$, the right side of (6.3) is $0$, so the residual must be
nonempty. Merely using $a$ alone is not a break. The symmetric cut holds at
$b$.

Equations (6.2)--(6.3) are the two-cell version of the $p668$ reset theorem:
an added donor over an UNSAT smaller support must create either a containment
break or a literal exclusive-supply break.

## 7. Nested-hole corridor theorem

Assume neither final endpoint value, applied alone to $W$, supplies either
$A$ or $B$. If a final $A$-witness omitted one edited position, it would
already exist after the other single edit. Hence every final $A$-witness
contains both edits; the same is true for $B$.

For $a<b$, the joint $A$-witness forces

\[
x_a,x_b\subseteq A,\qquad
w_i\subseteq A\quad(a<i<b).
\tag{7.1}
\]

The variables contain no $0x2000$ bit. Therefore a joint $B$-witness further
requires the maximal $B$-compatible fixed context around $[a,b]$ to contain
$0x2000$. These two conditions are exact for the existence of some joint
$A,B$ value pair before preservation of the other targets.

For the authenticated word:

- exactly $216$ incumbent cells are submasks of $A$;
- they form $202$ runs, $188$ of length one and $14$ of length two;
- (7.1) gives $13102$ raw supports:
  $12872$ at distance one, $216$ at distance two, and $14$ at distance three;
- the $B$-context test leaves $335$ supports:
  $325$ adjacent and $10$ at distance two, on $611$ physical positions;
- $330$ supports admit values non-provider at both endpoints, comprising
  exactly $555057$ hole-feasible ordered value pairs.

The $335$ supports, serialized in lexicographic order as one decimal
$p,q$ pair followed by a newline, have stream SHA-256

    40e75d1a48275ddd83a9dc14300da40be051dcd88a95eb19a1deac853ffdc26e.

## 8. Exact elimination of the genuinely non-provider branch

For each of the $330$ supports, delete the two variable cells. Every target
without a fixed witness in the resulting three runs is represented by its at
most three maximal forms. Because (7.1) confines both variables to the seven
bits of $A$, each ledger uses fourteen raw cell bits plus form selectors.

There are $325$ supports having a target with no literal form compatible
with $x_a,x_b\subseteq A$. Adding that target's empty menu makes the exact
CNF immediately UNSAT.

Only five supports survive this structural screen. Exact value replay gives:

| support | hole-feasible pairs | one-target elimination core |
|---|---:|---:|
| $(1211,1212)$ | $243$ | $0x0838$ |
| $(3026,3027)$ | $567$ | $0x0875$ |
| $(4156,4157)$ | $567$ | $0x047b$ |
| $(4380,4381)$ | $243$ | $0x085b$ |
| $(5463,5464)$ | $567$ | $0x087b$ |

After imposing the joint $A,B$ forms and both endpoint non-provider
conditions, none of the listed base pairs supplies its row's core target.
Thus each row has a one-target exclusive-supply obstruction.

An independent implementation constructs all fixed-run and affected-interval
labels directly, without using the primary maximal-form implementation. It
checks all $325$ structural eliminations and all

\[
243+567+567+243+567=2187
\]

live value pairs, finding zero universal pairs.

The five live systems were additionally materialized as literal DIMACS files
with complete maps. Their dimensions (variables, clauses) are

\[
(52,175),\ (54,224),\ (55,211),\ (41,133),\ (45,126).
\tag{8.1}
\]

No solver was invoked on these files. Their unsatisfiability is proved by the
independent direct-interval replay, not by a DIMACS solver verdict.

This proves the frozen H2 two-edit theorem in Section 1.

## 9. Provider-first boundary

The exact provider atlas contains $45770$ hole-provider position/value pairs
and $44421$ distinct provider moves. Exactly $284$ of them leave at most
seven holes. Their hole-count histogram for one through seven holes is

\[
(1,15,2,13,17,69,167).
\tag{9.1}
\]

The provider-first two-step result artifact exhausts those $284$ first moves
and finds no completing second substitution. The executed criterion was

    holes_after <= 7

despite a stale source comment suggesting a narrower condition.

If exactly one endpoint of a final pair is a source-hole provider, orient
that endpoint first. Hence a mixed provider/non-provider pair is not a new
unordered branch. Combining the provider result with Section 8 gives:

> Every hypothetical two-edit completion has a provider-first orientation
> whose intermediate word has at least eight holes.

The sweep result file does not record the executed source or binary hash, and
the currently present remote source/binary postdate the result. The
first-stage count agrees exactly with the independent provider atlas, and the
later code change is diagnostic/persistence logic rather than enumeration
logic. Nevertheless, a strict executable-provenance claim requires a capped
rerun. This caveat does not affect the hash-closed no-go in Section 8.

## 10. Authenticated artifacts

Source and provider boundary:

    scratch/k16_ejection_lns_h2_p110_20260730.word
      5234b77101ac1f22ec1802b4e1f5eccb6f0fc6f540efff9bbd0dc92da8c09fe7
    scratch/k16_h2_exact_provider_atlas.audit.json
      cd0a200e42013c43146369986ca946c3277cd2440c38219d2c45dd7305475754
    scratch/k16_h2_twostep_firsth7_debt7_to0.audit.json
      92c86bafea6e50630efa370e0cf048c69ecfcbb79178cda58bd1f343493d0225

Hash-closed non-provider atlas:

    scratch/audit_k16_h2_nonprovider_joint_supports_20260730.py
      d9c0ea24d6cf21bbb61314e83f757076c5a264f6a1650018d2f8f016f7d3a268
    scratch/k16_h2_nonprovider_joint_supports_20260730.audit.json
      bb9ff7812d69d7e9b95de51badb29f59b87a3ec012c7f7d8514c574608bcf2b8
      payload 58fd96b8b74c9e9a9a890ac95bcc739a013c358b41c7cf21d3f8f8c1991acc6a

Independent direct-interval audit:

    scratch/audit_k16_h2_nonprovider_joint_supports_independent_20260730.py
      44ee384f1f862aa57e3ed9441a8c457956053fbf43293bc1d550ef9605bac141
    scratch/k16_h2_nonprovider_joint_supports_independent_20260730.audit.json
      5d11ff16a66d638448a8e85b4a3ac1ea61134336a3f74bbfb748bf116a8482ef
      payload 5da33e78a916c57d5965cff53c8e97c07e8e56bbe6bafabe9faaf9cadc577865

Five exact DIMACS instances and maps:

    scratch/generate_k16_h2_nonprovider_tiny_cnfs_20260730.py
      db18607315051f9c171e835e0f2e64439dfa59dd81b9e52b675d14df4be994c5
    scratch/k16_h2_nonprovider_tiny_cnfs_20260730/manifest.json
      4a7c118d11aac8cd31bd8b7c94d40ecce55469db61a1e1d8cdbfc5e82c070241
      payload 4670995b7ded086675c5cfaeb6fc2af685f034ef79875843e7d08350b9249223

The DIMACS manifest freezes every individual CNF and map hash. Each formula
has seven live coordinate bits per endpoint, forced joint $A,B$ forms, two
cell-nonzero rows, and four endpoint-non-provider rows.

No heavy local process and no new H100 solve was launched for this theorem.
The two finite audits were lightweight exact replays.

## 11. Sharp remaining two-edit computation

The remaining question is not a generic $65535^2$ value search. Enumerate
only provider first moves whose intermediate hole count is at least eight.
For each intermediate word $V$ and each prospective last position $q$,
compute $L_q(V)$ and $U_q(V)$ from every target in $\mathcal S_q(V)$.

The branch is impossible unless

\[
U_q(V)\ne0,\qquad L_q(V)\subseteq U_q(V),
\]

and, when it survives, all possible last values form the single Boolean
interval $[L_q(V),U_q(V)]$. This exclusive-supply finish atlas is the exact
next computation. It is mathematically distinct from, and strictly more
compressed than, another provider-value sweep.
