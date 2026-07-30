# Explicit \(K=17\) upper bound from the verified \(K=16\) optimum

## Statement

Let \(\nu(k)\) be the minimum length of a word of nonempty subsets of
\([k]\) whose nonempty contiguous interval unions contain every nonempty
subset of \([k]\). The verified \(K=16\) word of length \(12873\) implies

\[
\boxed{\nu(17)\le 25746.}
\]

This is an explicit literal upper bound. It does **not** prove the
conjectured value \(B(17)=24313\).

## One-coordinate lift lemma

Let

\[
X=(x_0,x_1,\ldots,x_{L-1})
\]

be universal on \([k-1]\), and let \(z\) be a new coordinate. Define

\[
Y=(x_0,\ldots,x_{L-1}),\ \{z\},\
   (x_0\cup\{z\}),\ldots,(x_{L-2}\cup\{z\}).
\]

Then \(Y\) is universal on \([k]\) and has length \(2L\).

### Proof

Every target not containing \(z\) occurs in the first copy of \(X\).
The singleton \(\{z\}\) is an explicit cell. Now take a target
\(S\cup\{z\}\), with nonempty \(S\subseteq[k-1]\), and choose an interval
\(x_i\cup\cdots\cup x_j=S\).

- If \(j<L-1\), the corresponding interval in the marked copy has union
  \(S\cup\{z\}\).
- If \(j=L-1\), the suffix \(x_i,\ldots,x_{L-1}\) followed by the central
  cell \(\{z\}\) has union \(S\cup\{z\}\).

Thus every nonempty target occurs. \(\square\)

## Instantiation and retained artifacts

The authenticated parent is

scratch/k16_optimal_12873_20260731.word

with SHA-256

890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe.

The canonical retained child is

answers/k17_upper25746.word

and the construction-time copy is

scratch/k17_explicit_upper25746_from_k16_20260731.word

with SHA-256

f8ea81ab1f8f1280f638e7e607b32a7dd53fc541b30fe1005db8aae692be031b.

A literal replay against the canonical `answers/` path is retained as

scratch/k17_upper25746_answers_path_20260731.audit.json

with SHA-256
9c01743445a066579b04417be0a53150421f5978cc2cddf40ebdc70d1deda272.

The builder and exhaustive suffix-frontier verifier are

scratch/build_verify_k17_upper25746_from_k16_20260731.py

with SHA-256

16760d88b8decc06a74090aa44fe2b0967e05d6b86876fec0cfdb8316746ecac.

The retained primary audit is

scratch/k17_explicit_upper25746_from_k16_20260731.audit.json

with SHA-256

931e89c526d32641aea2ffc54ac6405bf536dff1329e3a666af4f8593e6182c6.

An independent literal replay additionally scanned \(103732303\) ordinary
contiguous interval extensions and covered exactly \(131071/131071\)
nonempty targets:

scratch/k17_explicit_upper25746_from_k16_20260731.independent.audit.json.

Its SHA-256 is

8b07b73a097fea54634e35cc29d7b02912c0f0cc6d612c812f66186edda3746c,
and its canonical payload SHA-256 is
15cea3d8801631b98da308a6eca32e7d154057b4f2cc51ad613eeb5c0d7b35c6.

A second independent verifier retained its result as

scratch/k17_explicit_upper25746_from_k16_independent_20260731.audit.json

with SHA-256
262fa4f9e03bf69603e6fdaf92a306cb6a0cb3aeb336c28f789bf9adf9014241.

## Current interval

The proved deadline lower bound gives \(B(17)=24313\). Consequently the
current certified interval becomes

\[
\boxed{24313\le \nu(17)\le25746},
\]

a gap of \(1433\). The protected-\(U\), decorated residual-pair campaign is
still targeting the lower endpoint \(24313\).
