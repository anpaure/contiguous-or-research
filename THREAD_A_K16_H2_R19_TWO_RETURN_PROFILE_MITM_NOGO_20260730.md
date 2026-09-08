# K16 H2 R19 two-return profile-MITM theorem and exact no-go

Date: 2026-07-30  
Lane: A  
Status: proved, independently code-audited, and exhaustively decided for the stated face

## 1. Frozen face

All positions below are zero-based. Let \(W\) be the authenticated
length-\(12873\) word

~~~text
scratch/k16_ejection_lns_h2_p110_20260730.word
SHA-256 5234b77101ac1f22ec1802b4e1f5eccb6f0fc6f540efff9bbd0dc92da8c09fe7.
~~~

Its only missing masks are \(0x4879,0x6879\). Choose one token position

\[
  e\in E=\{573,3044,3644,6090,6302,6725,10082,10277,10881\}
\]

and replace \(W_e\) by \(0x082a\). Independently replace position \(5462\)
by one of the eight service alleles

\[
  0x0018,0x0038,0x0058,0x0078,
  0x0818,0x0838,0x0858,0x0878.
\]

Every one of these \(9\cdot8=72\) two-edit bases has exactly the three holes

\[
  L=\{0x486b,0x686b,0x6c6b\}.
\]

The fixed-service return catalogue is

\[
\begin{aligned}
B_1&=[576,578],&B_2&=[3329,3331],&B_3&=[3494,3496],\\
B_4&=[3838,3840],&B_5&=[5463,5466],&B_6&=[5971,5973].
\end{aligned}
\]

Thus \(R=\bigcup_iB_i\) has \(19\) cells. The theorem permits an arbitrary
unordered pair \(p<q\) in \(R\), including two cells in the same block, and
arbitrary replacement values \(x,y\in[1,65535]\) different from the two
incumbent values respectively, namely \(x\ne W_p\) and \(y\ne W_q\).
Values may coincide and there is no Hamming, provider, or
intermediate-hole restriction. Every other cell is frozen.

This is the complete natural \(R19\) fixed-service face. It is not the old
displayed eighteen-cell face whose fifth block was \([5462,5464]\): that face
allows a return to overwrite the service cell. The present theorem neither
uses nor decides that service-overwrite face.

## 2. Exact two-return decomposition

For a target mask \(t\), let \(c(t)\) be its number of interval witnesses in
a fixed base word. For \(p<q\), partition the intervals meeting
\(\{p,q\}\) into the three nonempty incidence classes

\[
  \mathcal I_p,\qquad \mathcal I_q,\qquad \mathcal I_{pq},
\]

and put

\[
  K_{p,q}=\{t:\text{no witness interval for }t\text{ avoids both }p,q\}.
\]

Equivalently, if \(a_p(t),a_q(t),a_{pq}(t)\) count witnesses meeting \(p\),
meeting \(q\), and meeting both, then

\[
  t\in K_{p,q}\iff c(t)-a_p(t)-a_q(t)+a_{pq}(t)=0. \tag{2.1}
\]

For \(t\in K_{p,q}\), define exact Boolean profiles

\[
\begin{aligned}
X_t(x)&=1 &&\Longleftrightarrow
   \text{some interval in }\mathcal I_p\text{ has OR }t\text{ after }p\gets x,\\
Y_t(y)&=1 &&\Longleftrightarrow
   \text{some interval in }\mathcal I_q\text{ has OR }t\text{ after }q\gets y,\\
Z_t(s)&=1 &&\Longleftrightarrow
   \text{some interval in }\mathcal I_{pq}\text{ has OR }t
   \text{ when }x\mathbin{\lor}y=s.
\end{aligned}
\]

All profiles are computed from the literal left/right OR contexts; no
marginal or provider approximation is used.

**Lemma 2.1 (exact compatibility).** The word obtained by replacing
\(p\gets x,q\gets y\) is universal if and only if

\[
  X_t(x)\lor Y_t(y)\lor Z_t(x\lor y)=1
  \quad\text{for every }t\in K_{p,q}. \tag{2.2}
\]

If \(p,q\) lie in distinct \(B_i\), the \(Z\)-term vanishes on
\(K_{p,q}\), so (2.2) reduces exactly to \(X_t(x)\lor Y_t(y)=1\).

*Proof.* An interval avoiding both edits is unchanged. Hence targets outside
\(K_{p,q}\) remain covered, and every possible new witness for a target in
\(K_{p,q}\) lies in exactly one of the three displayed incidence classes.
This proves (2.2). Between consecutive return blocks the exact gap OR is
\(0x7fff\). Consequently every interval meeting two distinct blocks has OR
\(0x7fff\) or \(0xffff\). Those two masks have fixed avoiding witnesses,
respectively \([2,18]\) and \([6425,6436]\), so neither belongs to
\(K_{p,q}\). Thus \(Z\) contributes nothing for distinct blocks. For a
same-block pair it depends on both replacements only through \(x\lor y\),
and must be retained. \(\square\)

The same-block clause is essential. In the base \(e=573\), service
\(0x0018\), the pair \(p=576,q=577\) with

\[
  x=0x482b,\qquad y=0x086b
\]

individually supplies none of \(L\), while intervals containing both edits
supply all three masks in \(L\). Full replay still leaves fourteen other
holes. Thus a separable one-return product would be unsound in both
directions; (2.2) recognizes the joint supply and rejects the word only
after accounting for the collateral targets.

## 3. Maximum-envelope decision

Fix \(x\ne W_p\), and let \(D_x\subseteq K_{p,q}\) be the targets not covered
by the \(X\)-profile. Every completing value \(y\) must obey

\[
  y\subseteq T_x:=\bigcap_{t\in D_x}t, \tag{3.1}
\]

because an interval whose final OR is \(t\) cannot contain a bit outside
\(t\). In the same-block case, coverage below includes the joint
\(Z_t(x\lor y)\) term.

**Lemma 3.1 (maximum envelope).** For a fixed nonzero \(x\ne W_p\):

1. if \(D_x=\varnothing\), any allowed nonzero \(y\ne W_q\) completes;
2. if \(D_x\ne\varnothing\) and \(T_x=0\), no completion exists;
3. if \(T_x\ne W_q\), a completion exists if and only if \(y=T_x\)
   completes;
4. if \(T_x=W_q\), a completion exists if and only if one of the nonzero
   coatoms \(W_q\setminus\{b\}\), \(b\in W_q\), completes.

*Proof.* Suppose \(y\subseteq y'\subseteq T_x\). If a \(q\)-only interval
has OR \(t\in D_x\) at \(y\), then adding bits from \(T_x\subseteq t\) leaves
its OR equal to \(t\); the same argument applies to a both-cell interval
because \(x\lor y\subseteq x\lor y'\). Thus coverage is upward-monotone in
the Boolean interval \([y,T_x]\). This proves cases 1--3. In case 4, any
allowed completing \(y\ne W_q\) is a proper nonzero subset of \(W_q\), hence
is contained in a nonzero coatom of \(W_q\), which also completes by the
same monotonicity. \(\square\)

Consequently it is exhaustive to enumerate the \(65534\) allowed first
values, group identical first profiles, and test one envelope or at most
\(16\) coatoms for the second value. This is a solver-free profile
meet-in-the-middle decision, not a sampled search.

## 4. Exhaustion theorem

**Theorem 4.1 (R19 two-return no-go).** No word in the frozen face of
Section 1 is universal. Equivalently, none of the \(72\) token/service bases
can be completed by changing two distinct cells of \(R\) to arbitrary
allowed nonzero values.

*Proof.* Lemmas 2.1 and 3.1 reduce each fixed base and unordered position pair
to the finite exact profile test above. The audited engine exhausts

\[
\begin{aligned}
72\binom{19}{2}&=12312 &&\text{position kernels},\\
72\cdot150&=10800 &&\text{distinct-block kernels},\\
72\cdot21&=1512 &&\text{same-block kernels}.
\end{aligned}
\]

Here \(21=5\binom32+\binom42\), so every compatible same-block pair is
included. The theoretical first-value ledger has

\[
  12312\cdot65534=806854608
\]

rows. Exact profile equality reduces it to \(99,499,176\) first-profile
rows; the expanded logical ledger contains \(99,643,104\) second
envelope/coatom tests, with identity kernels then served from the exact
cache. The maximum
critical-set size is \(36\). There are \(297\) distinct full kernel keys; the
cache key contains \(K_{p,q}\), all \(X,Y,Z\) contexts, both incumbents, and
the same-block flag, so reuse is an identity quotient rather than an
assumption. Every one of the \(72\) case rows has exactly \(171=150+21\)
kernels. The final witness is null and the negative-run cardinality
assertions all pass. Therefore no permitted assignment satisfies (2.2).
\(\square\)

## 5. Authentication and independent audit

The implementation is

~~~text
scratch/search_threadA_k16_h2_tworeturn72_profile_mitm_20260730.cpp
SHA-256 644ff89cba87372db01420ba8c61c1794065e6c1a37c4677bf348d5db3f80fd3.
~~~

Two independent line audits found no semantic kernel error. They checked the
occurrence-count subtraction (2.1), context partition, same-block synergy,
distinct-block quarantine, profile grouping, cache key, and envelope/coatom
proof. Reduced literal replays agreed with the kernel for a same-block pair
and a distinct-block pair.

The capped H100 run used one CPU, /home only, a \(4\) GiB address-space cap,
a \(1\) GiB output cap, and no SAT solver. It took \(2.33\) seconds, used
\(7440\) KiB maximum resident memory, incurred no swap, and exited zero. A
fresh second run was byte-identical at the audit level. The preserved
artifacts are under

~~~text
scratch/threadA_k16_h2_tworeturn72_profile_mitm_20260730/
~~~

with principal hashes

~~~text
engine                  32549e9f299d2cb29589432e4b657904d5c123f56c4e2e991d899cad5f05c973
audit.json              fd6596aeb55e511a59a20ece0b5e8f8878f5fbd7e84f69a6934cb822902faad4
audit.rerun.json        fd6596aeb55e511a59a20ece0b5e8f8878f5fbd7e84f69a6934cb822902faad4
stderr.log              b1daa4161afcfc54d9f4ab46fc2b0fa5fc61d12b37eda2da7dca8cc72782d251
resource.txt            fcc2fc07252df0285231f935d78754a25ac3f9d00fa4b5bcb7c2da04ba125b61
~~~

No candidate word was emitted. Independent JSON aggregation reproduces all
totals in Theorem 4.1 and finds no malformed case row.

## 6. Exact boundary

The theorem closes the smallest complete two-return continuation of the nine
authenticated neutral tokens with the eight fixed service alleles and the
natural \(R19\) return catalogue. It proves no unrestricted length-\(12873\)
no-go. In particular it does not exclude

1. a donor/return cell outside \(R\);
2. a return that overwrites the service position \(5462\);
3. three or more return edits;
4. a different non-provider token or service architecture; or
5. a coherent global rethread not representable by this four-edit face.

The exact global bracket therefore remains

\[
  12873\le \nu(16)\le12874.
\]

Within this fixed token/service architecture, the next smallest branch
forced by this result is an expanded-support remote-return circuit: at least
one donor outside \(R19\), or at least three return edits, unless the
service-overwrite face is reopened explicitly.
