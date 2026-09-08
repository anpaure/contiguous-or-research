# K16 H2 internal debt-two donor and retained-R19 two-return theorem

Date: 2026-07-30  
Lane: A  
Status: proved, independently audited, and exhaustively negative for the stated face

## 1. Frozen source and exact quantifiers

All positions are zero-based.  Let $W$ be the authenticated length-$12873$
word

~~~text
scratch/k16_ejection_lns_h2_p110_20260730.word
SHA-256 5234b77101ac1f22ec1802b4e1f5eccb6f0fc6f540efff9bbd0dc92da8c09fe7
~~~

whose holes are $0x4879,0x6879$.  The exact-debt-two reserve atlas has two
rows whose donor cells lie inside the natural return set $R19$:

(All undelimited mask values below are hexadecimal.)

\[
\begin{array}{c|c|c|c}
d&W_d&\text{donor value}&\text{donor debts}\\\hline
3496&4862&082a&\{6c62,6e62\}\\
5971&094a&082a&\{494b,694b\}.
\end{array}                                                   \tag{1.1}
\]

Fix one row $d$, retain $V_d=0x082a$, and replace service cell $5462$
by one value in

\[
\mathcal Y=\{0018,0038,0058,0078,0818,0838,0858,0878\}.       \tag{1.2}
\]

Let

\[
R_d=R19\setminus\{d\},\qquad |R_d|=18.                       \tag{1.3}
\]

Choose exactly two distinct cells $p<q$ in $R_d$, and replace them by
arbitrary values

\[
a,b\in\{1,\ldots,65535\},\qquad a\ne V_p,\quad b\ne V_q.     \tag{1.4}
\]

The two values may coincide.  There is no Hamming, provider, or
intermediate-hole restriction.

The donor cell is deliberately not a return cell.  A no-op return there is
only a one-return case, while a genuine overwrite erases the retained donor;
both have final support at most three and belong to the separately active
support-at-most-three/radius-three lane.  Also excluded are $p6440$,
exterior returns, three or more returns, and global rethreads.  Thus every
word in this theorem has four distinct edited positions: donor, service, and
two returns.

This is the smallest complete remaining disjoint shell.  It has

\[
2\cdot8\binom{18}{2}=2448                              \tag{1.5}
\]

position kernels.  By comparison, even one exterior return over the already
audited low-debt bases has $2878624$ position instances; the two-return
one-$R19$-plus-one-exterior face has $54693856$ kernels.

## 2. The non-marginal base ledgers

**Lemma 2.1 (exact donor/service replay).**  For every service in (1.2), the
two internal donors produce different hole ledgers:

\[
\begin{aligned}
\operatorname{holes}(V^{3496})
  &=\{486b,686b,6c62,6c6b,6e62\},\\
\operatorname{holes}(V^{5971})
  &=\{494b,694b\}.                                           \tag{2.1}
\end{aligned}
\]

For donor $5971$, the three service-ladder masks are restored by the
literal intervals

\[
[5971,5973]=486b,\qquad
[5971,5974]=686b,\qquad
[5971,5975]=6c6b.                                           \tag{2.2}
\]

All $16\cdot5=80$ inter-$R19$ gap checks have OR $0x7fff$, and the
fixed avoiding intervals retain ORs

\[
[2,18]=0x7fff,\qquad[6425,6436]=0xffff.                      \tag{2.3}
\]

*Proof.*  Each of the sixteen donor/service bases is replayed from its full
contiguous-OR multiplicity ledger.  Equations (2.1)--(2.3) are asserted
against those literal counts; they are not obtained by adding separate donor
and service marginals.  The intervals in (2.2) give an independent direct
check of the unexpected second line of (2.1).  \(\square\)

The asymmetry in (2.1) is essential: a hard-coded five-hole or three-ladder
critical set would be wrong for half the bases.

## 3. Exact compatibility and envelope reduction

For a base $V$ and pair $p<q$, define

\[
K_{p,q}(V)=
\{T\ne0:\text{ no witness interval for }T\text{ avoids both }p,q\}. \tag{3.1}
\]

The engine computes this set afresh from the exact base multiplicities.
Partition intervals meeting the pair into $p$-only, $q$-only, and
both-cell classes, and let their exact profiles be

\[
X_T(a),\qquad Y_T(b),\qquad Z_T(a\lor b).                    \tag{3.2}
\]

**Lemma 3.1 (exact two-cell criterion).**  The edited word is universal if
and only if

\[
X_T(a)\lor Y_T(b)\lor Z_T(a\lor b)=1
\qquad(T\in K_{p,q}(V)).                                    \tag{3.3}
\]

*Proof.*  Targets outside $K_{p,q}(V)$ retain an unchanged avoiding
witness.  Every possible new witness for a critical target lies in exactly
one of the three displayed incidence classes.  \(\square\)

The $Z$-term is retained exactly when a literal both-cell context can be
active under the nonzero/changed restrictions.  Namely, for fixed context
OR $c$ and target $T$, such values exist exactly when

\[
c\subseteq T\quad\text{and}\quad
\bigl(|T|\ge2\ \text{or}\ (T\ne V_p\text{ and }T\ne V_q)\bigr). \tag{3.4}
\]

The proof is the singleton/proper-coatom argument from the preceding
exact-two theorem.  In the present physical census, all $2144$ cross-block
kernels are joint-inactive and all $304$ same-block kernels are
joint-active.

For fixed $a$, let $D_a\subseteq K_{p,q}(V)$ be the targets not supplied
by $X(a)$, and put

\[
T_a=\bigcap_{T\in D_a}T.                                    \tag{3.5}
\]

Any completing $b$ satisfies $b\subseteq T_a$.  Coverage by $Y(b)$ or
$Z(a\lor b)$ is upward-monotone while $b\subseteq T_a$.  Hence it is
exhaustive to test $T_a$, or its nonzero coatoms when $T_a$ is the
forbidden incumbent $V_q$.  If $T_a=0$, no nonzero completing value exists,
so that first-profile representative is rejected; $D_a=\varnothing$ is
already complete.  Joint-inactive kernels may group identical
$X$-profiles, while joint-active kernels retain every literal first value
because $Z$ also depends on $a\lor b$.

This is a deterministic maximum-envelope/coatom MITM, not a provider-only
filter or a random search.

## 4. Exact exhaustion

**Theorem 4.1 (internal-donor no-go).**  No word satisfying all quantifiers
of Section 1 is universal.

*Proof.*  Lemmas 2.1 and 3.1 and the envelope monotonicity reduce every
allowed assignment to a complete finite profile kernel.  Each of the
sixteen bases has

\[
\binom{18}{2}=153=134+19                                  \tag{4.1}
\]

kernels, with $134$ cross-block and $19$ same-block pairs.  The complete
ledger is

\[
\begin{aligned}
16\cdot153&=2448=2144+304,\\
2448\cdot65534&=160427232
\end{aligned}                                               \tag{4.2}
\]

raw first-value rows.  Exact compression retains $20003712$ first rows and
tests $20008232$ second envelopes/coatoms.  There are $544$ exact kernel
keys and $1904$ identity-cache hits.  The largest critical set has size
$38$; the implementation fails closed above $64$.

All sixteen bases and all $2448$ kernels are visited.  There are $264$
compressed first-profile representatives with $T_a=0$, no empty-deficit
shortcut, and no positive witness.  Therefore (3.3) fails for every allowed
pair of values.  \(\square\)

**Corollary 4.2.**  Combining Theorem 4.1 with the preceding ordinary-donor
theorem closes all twenty authenticated collateral-exactly-two reserve donor
rows, all eight fixed services, and exactly two distinct $R19$ return edits
which do not overwrite the retained donor.

## 5. Authentication

The final engine is

~~~text
scratch/search_threadA_k16_h2_internal_debt2_r19_tworeturn_mitm_20260730.cpp
SHA-256 93ffc1554d4eaa9b0e8eda883966c8f9ac320c06bd23880e0bb6366c781748ce
~~~

and includes the previously audited R19 kernel source with SHA-256

~~~text
644ff89cba87372db01420ba8c61c1794065e6c1a37c4677bf348d5db3f80fd3.
~~~

An independent pre-run line audit found the donor-$5971$ ledger asymmetry,
checked the corrected source, and verified the quantifiers, dynamic critical
set, joint-activity condition, cache identity, counters, and the full-replay
branch required for any positive candidate.  A separate copied-artifact
aggregation independently checked every case row and all totals.

Two fresh executions used one H100 CPU in a unique `/home` directory, a
$4$ GiB address-space cap, $1$ GiB output cap, and $1800$-second
timeout.  They exited zero in $0.77$ and $0.73$ seconds, used $7588$
and $7592$ KiB maximum resident memory, incurred no swap, emitted no
candidate, and produced byte-identical audits:

~~~text
scratch/threadA_k16_h2_internal_debt2_r19_tworeturn_mitm_20260730/run1.audit.json
scratch/threadA_k16_h2_internal_debt2_r19_tworeturn_mitm_20260730/run2.audit.json
SHA-256 2a681cb967a80b1fbdc72f5bae9e4c304d403eeef486e70667a9b09bdc8c24d2
~~~

The compiled binary has SHA-256

~~~text
daee7c1df9cb8e726f784e40da6a1f4107275cf622ced4bac6fbf8771d0501d6.
~~~

Compiler identity, commands, exit codes, resource logs, and the complete hash
manifest are preserved in the same directory.

## 6. Exact boundary

The theorem decides only the retained-donor, exactly-two-return shell of
Section 1.  It does not decide:

1. one return, or a return which overwrites the donor cell (the
   support-at-most-three/radius-three lane);
2. a return outside $R19$;
3. collateral at least three;
4. three or more returns;
5. Lane D's $p6440$ service strata; or
6. any global rethread outside this fixed chronology.

Among the two alternatives in this dispatch, and within the
collateral-at-most-two catalogue, the remaining extension is the
outside-$R19$ return face; it still requires a new context-signature
compression to avoid its $54693856$ raw position-pair kernels.  The separate
collateral-exactly-three shell is also open and may be smaller.

No global bound changes.  The exact bracket remains

\[
12873\le\nu(16)\le12874.
\]
