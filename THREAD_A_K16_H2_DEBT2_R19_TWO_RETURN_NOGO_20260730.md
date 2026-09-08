# K16 H2 exact-debt-two donor and R19 two-return theorem

Date: 2026-07-30  
Lane: A  
Status: proved and exhaustively decided for the stated face; no universal word

## 1. Frozen source and the one-notch choice

All positions are zero-based.  Let $W$ be the authenticated word

~~~text
scratch/k16_ejection_lns_h2_p110_20260730.word
SHA-256 5234b77101ac1f22ec1802b4e1f5eccb6f0fc6f540efff9bbd0dc92da8c09fe7
~~~

of length $12873$.  Its only holes are

\[
P=0x4879,\qquad Q=0x6879,
\]

and $E=0x082a$ has multiplicity one.  A *nonprovider $E$-reserve
donor* is a one-cell replacement $r\gets x$ which creates a second
witness of $E$ while keeping $P,Q$ absent.  Its collateral set
$D(r,x)$ consists of all formerly covered masks whose multiplicity becomes
zero.

There were two proposed next enlargements of the preceding low-debt theorem:

1. allow the next collateral stratum of donors; or
2. retain the old donors and allow a return outside $R19$.

The smallest complete next face is the exact stratum $|D|=2$.  It has
only $18$ operative donor rows and $24624$ two-return kernels.  By
contrast, even the one-exterior-return census over the already audited
$224$ low-debt donor/service bases has

\[
224\cdot12851=2878624>116\cdot24624
\]

port instances.  That one-return face is the separately quarantined
unrestricted radius-three lane.  Among the present two-return extensions,
the complete face using one $R19$ return and one exterior return has

\[
224\cdot19\cdot12851=54693856>2221\cdot24624             \tag{1.1}
\]

position kernels.  Here $12851=12873-19-1-1-1$: the $R19$ cells,
the donor, service cell, and Lane-D cell $6440$ are omitted.  This count
cannot be reduced by the elementary current-hole provider filter: at every
remaining cell, replacing the singleton by any current hole gives that hole
a witness and differs from the incumbent because the mask was absent.
Thus a useful reduction of the exterior-return face would first require a
new context-signature dominance theorem.

This note therefore decides collateral *exactly two*.  It does not claim to
decide the full $|D|\ge2$ atlas, which has $13089$ rows.

## 2. Exact donor catalogue and service ledger

The fixed return set is

\[
\begin{aligned}
B_1&=[576,578],&B_2&=[3329,3331],&B_3&=[3494,3496],\\
B_4&=[3838,3840],&B_5&=[5463,5466],&B_6&=[5971,5973],
\end{aligned}
\]

and $R19=\bigcup_iB_i$ has $19$ cells.  Position $5462$, the service
cell, is not in $R19$.

**Theorem 2.1 (complete exact-two shell).**  The authenticated reserve atlas
has exactly $20$ donor rows with $|D|=2$.  Two have donor cells already
inside $R19$:

\[
3496:082a\mapsto\{6c62,6e62\},\qquad
5971:082a\mapsto\{494b,694b\}.
\]

After excluding those overlapping donor/return rows, the operative shell is
the following $18$ rows on $17$ positions.  Values and masks are
hexadecimal.

\[
\begin{array}{r|r|l@{\qquad}r|r|l}
r&x&D(r,x)&r&x&D(r,x)\\\hline
240&082a&012a,09aa&935&082a&182a,1c2a\\
2293&082a&0e6a,0e6b&2685&082a&0ce9,0ced\\
3310&082a&083a,083e&3929&0822&313a,353a\\
4779&082a&3a62,3a72&5384&082a&1aac,3aac\\
6089&0028&1caa,1eaa&6089&0828&1caa,1eaa\\
6091&0828&1caa,1cab&6678&082a&812a,89aa\\
8731&082a&8e6a,8e6b&8732&082a&9c6a,bc6a\\
9934&082a&ec62,ee62&11822&082a&9aac,baac\\
12409&082a&c94b,e94b&12872&082a&ce61,ce63
\end{array}
\]

For every row and every service value

\[
\mathcal Y=\{0018,0038,0058,0078,0818,0838,0858,0878\},       \tag{2.1}
\]

replace the donor cell and then replace cell $5462$ by $y\in\mathcal Y$.
The resulting base $V$ has exactly

\[
\operatorname{holes}(V)=
\{0x486b,0x686b,0x6c6b\}\cup D(r,x),                         \tag{2.2}
\]

five distinct masks.  There are $18\cdot8=144$ bases and $17$
distinct five-hole sets.  Every one of the $144\cdot5=720$ modified
inter-$R19$ gap checks has OR $0x7fff$.

*Proof.*  The reserve atlas exhausts every nonzero value at every source
position that creates the required second $E$-witness while preserving
the two source holes.  Filtering its accepted rows by exact collateral
cardinality two gives the stated twenty rows; literal position filtering
gives the eighteen displayed rows.  The compact filtered-row hashes are

\[
\begin{array}{c|c}
\text{all exact-two rows}&
f7a805e32404c376901388574fc648acc65f45e27bf9ff3db5a16d4a8f5d293a\\
\text{operative full rows}&
4c17055b790fd0be53a328e77f9951743570c6bd33851ab6b97b353798cd1545\\
\text{operative }(r,x,D)\text{ triples}&
4f120dd86219bc1222908753997b5a77aa8791ba18f7926cb7a475486d9b2aac.
\end{array}
\]

For each of the $144$ bases, a fresh full interval-multiplicity replay
gives (2.2), rather than inferring it from separate donor and service
marginals.  The same replay verifies all gap ORs.  The independently frozen
catalogue summary is

~~~text
scratch/threadA_k16_h2_debt2_r19_catalogue_20260730.audit.json
SHA-256 c705d0df93235a6c40c83aca436b9bb4519d74e567cada614be34a625a7a0a3c
~~~

This shell has no exact position/value overlap with Lane D's retained
$p6440$ service atlas.  Position $6440$ is never edited here.  Every
case has four distinct sites: donor, service, and two return cells.
\(\square\)

## 3. Exact two-return compatibility

Fix one base $V$, two distinct return cells $p<q$ in $R19$, and
replacement values

\[
a,b\in\{1,\ldots,65535\},\qquad a\ne V_p,\quad b\ne V_q.       \tag{3.1}
\]

The values may coincide.  No Hamming, provider, or intermediate-hole
restriction is imposed.

For a target $T\ne0$, let $c(T)$ be its witness multiplicity in $V$.
Partition intervals meeting $\{p,q\}$ into $p$-only, $q$-only, and
both-cell classes.  Put

\[
K_{p,q}(V)=\{T:\text{no witness of }T\text{ avoids both }p,q\}. \tag{3.2}
\]

From the literal fixed interval contexts define $X_T(a)$, $Y_T(b)$,
and $Z_T(a\lor b)$ to assert the existence of a $p$-only, $q$-only,
or both-cell witness of $T$, respectively.

**Lemma 3.1 (exact compatibility).**  The twice-edited word is universal if
and only if

\[
X_T(a)\lor Y_T(b)\lor Z_T(a\lor b)=1
\qquad(T\in K_{p,q}(V)).                                    \tag{3.3}
\]

*Proof.*  A target outside $K_{p,q}(V)$ retains an avoiding witness.
Every possible new witness of a target in $K_{p,q}(V)$ belongs to exactly
one of the three interval classes.  This is precisely (3.3).  \(\square\)

The implementation does not infer whether the $Z$-term is relevant from
block names.  For a both-cell interval with fixed-context OR $c$, it tests
the following exact condition.

**Lemma 3.2 (joint activity).**  There exist allowed values satisfying
$c\lor a\lor b=T$ if and only if

\[
c\subseteq T\quad\text{and}\quad
\bigl(|T|\ge2\ \text{or}\ (T\ne V_p\text{ and }T\ne V_q)\bigr). \tag{3.4}
\]

*Proof.*  Necessity is immediate.  For a singleton $T$, its only nonzero
submask is $T$, so both changed values must equal it.  For $|T|\ge2$,
the mask $T$ and two proper nonzero submasks whose union is $T$ let one
avoid the one forbidden incumbent at each endpoint.  Together with
$c\subseteq T$, their OR is $T$.  \(\square\)

In the exact census, (3.4) makes all $21600$ cross-block kernels
joint-inactive and all $3024$ same-block kernels joint-active.  Thus the
same-block $a\lor b$ synergy is retained in every case, while cross-block
suppression is a checked consequence of the physical $0x7fff$ separators
and fixed avoiding witnesses.

## 4. Complete maximum-envelope reduction

Fix $a\ne V_p$.  Let $D_a\subseteq K_{p,q}(V)$ be the targets not
covered by $X(a)$, and set

\[
T_a=\bigcap_{T\in D_a}T.                                    \tag{4.1}
\]

**Lemma 4.1 (envelope/coatom test).**

1. If $D_a=\varnothing$, any allowed second value completes (3.3).
2. If $D_a\ne\varnothing$ and $T_a=0$, no completion exists.
3. If $T_a\ne0,V_q$, a completion exists exactly when $b=T_a$
   completes (3.3).
4. If $T_a=V_q$, a completion exists exactly when a nonzero coatom of
   $V_q$ completes (3.3).

*Proof.*  Any completing $b$ must satisfy $b\subseteq T$ for every
$T\in D_a$, hence $b\subseteq T_a$.  If
$b\subseteq b'\subseteq T_a$, adding bits from $T_a\subseteq T$ cannot
change a successful $q$-only interval OR away from $T$; the same is true
of a both-cell interval because $a\lor b\subseteq a\lor b'$.  Coverage is
therefore upward-monotone inside $[b,T_a]$.  This proves the first three
claims.  In the last case, any allowed proper nonzero subset of $V_q$ lies
below a nonzero coatom, which remains completing by monotonicity.
\(\square\)

It is consequently exhaustive to enumerate all $65534$ allowed first
values.  In joint-inactive kernels, identical exact $X$-profiles may be
grouped.  In joint-active kernels every literal first value is retained,
because the $Z$-term also depends on $a\lor b$.  For each retained first row,
only the maximum second envelope or its coatoms need be tested.  This is a
deterministic meet-in-the-middle decision; no SAT solver, random sample, or
provider-only filter is used.

## 5. Exhaustion theorem

**Theorem 5.1 (exact-two/R19 no-go).**  For none of the $144$ bases in
Theorem 2.1 do two distinct arbitrary-value return edits in $R19$ produce
a universal word.

*Proof.*  Lemmas 3.1, 3.2, and 4.1 reduce every base and unordered return
pair to an exact finite profile kernel.  The complete ledger is

\[
\begin{aligned}
144\binom{19}{2}&=24624 &&\text{kernels},\\
144\cdot150&=21600 &&\text{cross-block kernels},\\
144\cdot21&=3024 &&\text{same-block kernels},\\
24624\cdot65534&=1613709216 &&\text{raw first-value rows}.
\end{aligned}
\]

Every case contributes exactly $171$ kernels.  Exact profile equality
compresses the ledger to $199042176$ first-profile rows and
$199052752$ envelope/coatom tests.  There are $5049$ distinct exact
kernel keys and $19575$ identity-cache hits.  The cache key includes the
critical target list, all active $X,Y,Z$ contexts, both incumbent values,
and the semantic joint-activity flag.  The largest critical set has size
$38$, below the fail-closed limit $64$.

All $144$ bases and all $24624$ pairs were visited.  The final witness is
null, and the negative-run assertions reproduce every displayed count.
Hence (3.3) fails for every permitted assignment.  \(\square\)

## 6. Authentication and audit

The source is

~~~text
scratch/search_threadA_k16_h2_debt2_r19_tworeturn_mitm_20260730.cpp
SHA-256 478ea18ed7820fe89d9b08a38226e367aec978b163f13aafad2a7e879b76ed1e
~~~

and includes the previously audited R19 kernel source with SHA-256

~~~text
644ff89cba87372db01420ba8c61c1794065e6c1a37c4677bf348d5db3f80fd3.
~~~

Independent line audits checked the complete catalogue, fresh five-hole
replay, critical-set subtraction, exact joint-activity test, cache key,
envelope/coatom completeness, positive full replay, and all exhaustion
counters.  They found no semantic defect.

Two fresh executions used one H100 CPU in a unique `/home` directory, a
$4$ GiB address-space cap, a $1$ GiB output cap, and a $1800$-second
timeout.  Each exited zero in about $6.9$ seconds, used $8876$ KiB
maximum resident memory, and incurred no swap.  They emitted no candidate
word and produced byte-identical audits:

~~~text
scratch/threadA_k16_h2_debt2_r19_tworeturn_mitm_20260730/engine
  SHA-256 21138f0cb2742e900f4e623c69bf3305d803c128dcd3db274d03bdc27f6f96f4
scratch/threadA_k16_h2_debt2_r19_tworeturn_mitm_20260730/run1.audit.json
scratch/threadA_k16_h2_debt2_r19_tworeturn_mitm_20260730/run2.audit.json
  SHA-256 39defecf22fc97f83b597eb1a07a3dac0a37a826987ff5e3808378c69fe76203
~~~

The local manifest, resource logs, exit codes, compiler identity, and remote
command are preserved in the same directory.  The audit reports

~~~text
PASS_EXHAUSTED_UNSAT
cases=144 kernels=24624 unique=5049
profiles=199042176 envelopes=199052752 maxK=38
~~~

## 7. Exact proved/open boundary

The theorem is complete for:

- every authenticated nonprovider $E$-reserve donor outside $R19$ with
  collateral *exactly two*;
- each of the eight fixed service alleles at position $5462$; and
- exactly two distinct arbitrary-value return edits in $R19$.

It does not decide:

1. a one-return completion of an exact-two base (the deliberately separate
   unrestricted radius-three lane);
2. either exact-two donor whose donor cell lies inside $R19$;
3. collateral at least three, or the full $|D|\ge2$ atlas;
4. a return outside $R19$;
5. three or more return edits;
6. Lane D's $p6440$ service strata; or
7. a coherent global rethread outside this fixed chronology.

Thus this is a new exact branch no-go, not a proof that length $12873$ is
impossible.  The global bracket remains

\[
12873\le\nu(16)\le12874.
\]
