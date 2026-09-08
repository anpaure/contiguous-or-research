# Exact19 and exact20: independent forward literal certificates

2026-09-09. Verification by `exact_b_finite_frontier` of the two literal
files supplied by the user in Downloads. **Both pass.** Combined with
the established endpoint lower theorem, these witnesses prove

    nu(19)=B(19)=92,381,
    nu(20)=B(20)=184,759.

This verifies the supplied literal words, independently of any proposed
generator or structural proof. It does not prove equality in every
dimension. Together with the already authoritative exact results through
18, the finite exact frontier is now through20; the next dimension is21.

## 1. Executed fixed test and exact results

The standalone source is
[verify_k19_k20_optimal_forward_first_occurrence_20260909.py](verify_k19_k20_optimal_forward_first_occurrence_20260909.py).
Root and `exact_b_induction` independently read its complete source and
passed it before execution. It imports no previous verifier. One process
ran on H100 host `arboghast`, with no retry, alternative input, search,
suffix recurrence, segment tree, or cyclic extension.

| Dimension | Literal length | Distinct nonempty interval ORs | Missing | Forward change events |
|---|---:|---:|---:|---:|
|19|92,381|524,287|0|1,200,848|
|20|184,759|1,048,575|0|2,494,149|

Every letter is nonzero and inside the stated cube. Every rank j has
exactly binom(k,j) distinct realized targets. The checker explicitly
checks every target index, rather than inferring coverage solely from
the cardinality of a potentially malformed set.

Source SHA256:

    80731cc8e453cbfaf9225a403ec62620a4e056bec8d0c31413d218440d81a797

Raw user-input hashes, retained unchanged in the artifact bundle:

    k19_optimal92381.word, 598,636 bytes:
    1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414

    k20_optimal184759.word, 1,246,071 bytes:
    047b990b9e9f7a4585ba5d8fadf9c3d191cd218c989c3ffacf6e351d91b88d02

The hard limits were60 CPU seconds,90 wall seconds,1 GiB address space
and256 MiB per output file. Actual total measured time was
1.804267801 CPU seconds and1.804852370172739 wall seconds. The final
complete certificate has status PASS for both full-cube checks and
both exact all-rank lower-bound comparisons.

## 2. Why the enumeration is complete and ordinary

For a fixed ordinary start i and coordinate c, let p_c(i) be its first
occurrence at or after i, or a sentinel when none exists. For every
ordinary endpoint j>=i, the interval OR contains c exactly when
p_c(i)<=j. Thus its OR can change only at the distinct finite p_c(i).
At each such position, ALL coordinates sharing that first-occurrence
position must be added together: no partial letter is realizable.

The program maintains p_c(i) by decreasing the start i. Its actual
enumeration for that start proceeds forward through the sorted event
positions, recording the cumulative union after each complete group.
Every recorded mask is therefore an actual ordinary interval OR, and
every nonempty ordinary interval OR is one of the recorded masks. The
nonempty-letter check ensures the first event is at i. Endpoints always
satisfy0<=i<=j<N; no wrapping occurs.

For every target, the first encountered valid start/end pair is saved.
The complete witness arrays are part of the copied bundle. They are
produced by this forward method; the root's separately prepared
suffix/segment-tree verification is an independent lane and is not
claimed as an operation of this checker.

## 3. All-rank integer lower bounds

For every s=1,...,k, the checker computes

    M_s=binom(k,s),
    Lambda_s=sum_(j=1)^(s-1) binom(k,j),
    tau_s=min{t>=0: t*M_s+t*(t+1)/2>=Lambda_s}.

An integer square root gives a lower starting value for tau_s. The
program then checks both the attained capacity and the strictly failing
capacity at tau_s-1. Consequently each recorded tau_s is minimal by
exact integer arithmetic. Taking the maximum of M_s+tau_s over EVERY
rank gives the endpoint lower bound B(k); no central-maximizer premise
is required by this numerical step.

In both dimensions the unique maximizing rank is10:

|k|M_10|Lambda_10|Capacity at t=2|Capacity at t=3|B(k)|
|---|---:|---:|---:|---:|---:|
|19|92,378|262,143|184,759|277,140|92,381|
|20|184,756|431,909|369,515|554,274|184,759|

These independently computed values equal the verified literal lengths.
The mathematical lower theorem is the established endpoint theorem in
[Master Section2](../MASTER_HANDOFF.md); the report retains the exact
rows for every rank, including both minimality inequalities.

## 4. Complete copied artifacts

All files are copied locally under
[k19_k20_optimal_forward_20260909](k19_k20_optimal_forward_20260909/).
The remote execution directory is
`/home/amodo/exact-b-k19-k20-optimal-forward-20260909`.

The main report is
[k19_k20_forward_complete_certificate.json](k19_k20_optimal_forward_20260909/k19_k20_forward_complete_certificate.json).
Individual reports are
[k19_forward_certificate.json](k19_k20_optimal_forward_20260909/k19_forward_certificate.json)
and
[k20_forward_certificate.json](k19_k20_optimal_forward_20260909/k20_forward_certificate.json).
Both exact raw words are also retained there.

Each dimension has two target-indexed little-endian signed-int32 arrays,
`kK_ordinary_witness_start.int32` and `kK_ordinary_witness_end.int32`.
Index0 is unused. Entry T in the two arrays supplies the zero-based
inclusive ordinary interval for target T. Their complete hashes and
byte lengths are in both the individual and combined reports. Total
array size is4 MiB for k19 and8 MiB for k20.

The preceding k19 proper-pair/backbone work remains a general conditional
compiler interface; k19 is no longer an unresolved exact dimension after
these literal checks. No further construction or search was performed.
